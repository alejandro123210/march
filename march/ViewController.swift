//
//  ViewController.swift
//  march
//
//  Created by Alejandro Gonzalez on 4/7/18.
//  Copyright © 2018 dostuff. All rights reserved.
//

import UIKit
import MapKit
import Firebase

class ViewController: UIViewController, UICollectionViewDelegate, UICollectionViewDataSource, CLLocationManagerDelegate {

    @IBOutlet weak var collectionView: UICollectionView!
    var eventList: [Event] = []
    var eventListToShow: [Event] = []
    private var locationManager: CLLocationManager!
    private var currentLocation: CLLocation?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        collectionView.delegate = self
        collectionView.dataSource = self
        
        //geostuff
        locationManager = CLLocationManager()
        locationManager.delegate = self
        locationManager.desiredAccuracy = kCLLocationAccuracyBest
        if CLLocationManager.locationServicesEnabled() {
            locationManager.requestWhenInUseAuthorization()
            locationManager.startUpdatingLocation()
        }
        
        //firebase
        let ref = Database.database().reference(withPath: "array")
        ref.observeSingleEvent(of: .value, with: { snapshot in
            if !snapshot.exists() {return}
            let myArray: Array = snapshot.value as! Array<Any>
            let myArrayLength = myArray.count - 1
            for index in 0...myArrayLength{
                let stringForNumber = String(describing: index)
                let name = snapshot.childSnapshot(forPath: stringForNumber).childSnapshot(forPath: "name").value as! String
                let eventDescription = snapshot.childSnapshot(forPath: stringForNumber).childSnapshot(forPath: "descriptor").value as! String
                let location = snapshot.childSnapshot(forPath: stringForNumber).childSnapshot(forPath: "location").value as! String
                let time = snapshot.childSnapshot(forPath: stringForNumber).childSnapshot(forPath: "time").value as! String
                let tagString = snapshot.childSnapshot(forPath: stringForNumber).childSnapshot(forPath: "tags").value as! String
                let tags = tagString.components(separatedBy: ",")
                let pic = snapshot.childSnapshot(forPath: stringForNumber).childSnapshot(forPath: "pic").value as! String
                let event = Event.init(nam: name, eventDescriptio: eventDescription, locatio: location, tim: time, tag: tags, imag: pic)
                self.eventList.append(event)
            }
            //checks for charities in area
            for item in self.eventList{
                var locationToFind: CLLocationCoordinate2D?
                let geocoder = CLGeocoder()
                geocoder.geocodeAddressString(item.location!) {
                    placemarks, error in
                    let placemark = placemarks?.first
                    let lat = placemark?.location?.coordinate.latitude
                    let lon = placemark?.location?.coordinate.longitude
                    locationToFind = CLLocationCoordinate2D.init(latitude: lat!, longitude: lon!)
                    item.locationOfEvent = locationToFind!
                    item.lat = locationToFind?.latitude
                    item.long = locationToFind?.longitude
                    let mapPointA = MKMapPointForCoordinate(locationToFind!)
                    let mapPointB = MKMapPointForCoordinate((self.locationManager.location?.coordinate)!)
                    item.distance = MKMetersBetweenMapPoints(mapPointA, mapPointB)
                    item.daysTillDate = self.daysBetweenDates(dateString: item.time!)
                    if (item.daysTillDate! >= -1){
                        self.eventListToShow.append(item)
                    }
                    self.eventListToShow.sort(by: {$0.daysTillDate! < $1.daysTillDate!})
                    self.collectionView.reloadData()
                }
            }
        })
    }

    

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "Cell", for: indexPath) as! CustomCollectionViewCell
        let event = eventListToShow[indexPath.row]
        cell.event = event
        event.locationOfEvent = CLLocationCoordinate2DMake(event.lat! as CLLocationDegrees, event.long! as CLLocationDegrees)
        var imageView: UIImageView = cell.viewWithTag(1001) as! UIImageView
        //decode image
        if let dataDecoded : Data = Data(base64Encoded: event.image!, options: .ignoreUnknownCharacters) {
            if let decodedimage:UIImage = UIImage(data: dataDecoded) {
                imageView.image = decodedimage
            }
        }
        
        let nameLabel = cell.viewWithTag(1) as! UILabel
        print("LOOK HERE \(event.name!)")
        nameLabel.text = event.name!
        nameLabel.layer.zPosition = 10
        
        let distLabel = cell.viewWithTag(11) as! UILabel
        let distanceInMiles = event.distance! / 1609.34
        let myString = String(format: "%.1f", distanceInMiles)
        distLabel.text = "\(myString)mi"
        distLabel.layer.zPosition = 10
        
        let timeLabel = cell.viewWithTag(12) as! UILabel
        timeLabel.text = formatDate(date: event.time!)
        timeLabel.layer.zPosition = 10
        
        cell.layer.cornerRadius = 12
        
        return cell
    }

    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return eventListToShow.count
    }
    
    
    func daysBetweenDates(dateString: String) -> Int
    {
        let date = Date()
        let dateFormatter = DateFormatter()
        dateFormatter.locale = Locale(identifier: "en_US")
        dateFormatter.dateFormat = "MM/dd/yy hh:mma"
        let endDate = dateFormatter.date(from: dateString)
        let diffInDays = Calendar.current.dateComponents([.day], from: date, to: endDate!).day
        return diffInDays!
    }
    
    func formatDate(date: String) -> String{
        
        let dateFormatter = DateFormatter()
        dateFormatter.locale = Locale(identifier: "en_US")
        dateFormatter.dateFormat = "MM/dd/yy hh:mma"
        let dateVariable = dateFormatter.date(from: date)
        let printDateFormatter = DateFormatter()
        printDateFormatter.dateFormat = "MMMM dd, \nhh:mma"
        return printDateFormatter.string(from: dateVariable!)
        
    }

}
