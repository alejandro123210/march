//
//  CustomCollectionViewCell.swift
//  march
//
//  Created by Alejandro Gonzalez on 4/7/18.
//  Copyright © 2018 dostuff. All rights reserved.
//

import UIKit
import MapKit

class CustomCollectionViewCell: UICollectionViewCell {
    
    @IBOutlet weak var imageView: UIImageView!
    @IBOutlet weak var distLabel: UILabel!
    @IBOutlet weak var nameLabel: UILabel!
    @IBOutlet weak var timeLabel: UILabel!
    var delegate: HeaderCollectionViewCellDelegate!
    var event: Event?
    
    override func awakeFromNib() {
        
        self.backgroundColor = UIColor.white.withAlphaComponent(0.7)
        
        //image view gradient stuff
        let view = UIView(frame: imageView.frame)
        let gradient = CAGradientLayer()
        gradient.frame = view.bounds
        gradient.colors = [UIColor.clear.cgColor, UIColor.black.cgColor]
        view.layer.insertSublayer(gradient, at: 0)
        imageView.addSubview(view)
    }
    
    @IBAction func infoButton(_ sender: Any) {
        self.delegate.didClickInfo(sender: sender, event: event!)
    }
    
    
    @IBAction func directionsButton(_ sender: Any) {
        let placemark = MKPlacemark.init(coordinate: (event!.locationOfEvent!))
        self.getDirections(place: placemark)
    }
    
    @IBAction func shareButton(_ sender: Any) {
        self.delegate.didClickShare(sender: sender, event: event!)
    }
    
    private func getDirections(place: MKPlacemark){
        let mapItem = MKMapItem(placemark: place)
        mapItem.name = event?.name!
        mapItem.openInMaps(launchOptions: [MKLaunchOptionsDirectionsModeKey: MKLaunchOptionsDirectionsModeDefault])
    }
}

protocol HeaderCollectionViewCellDelegate {
    func didClickShare(sender: Any, event: Event)
    func didClickInfo(sender: Any, event: Event)
}


