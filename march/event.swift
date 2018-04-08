//
//  event.swift
//  march
//
//  Created by Alejandro Gonzalez on 4/7/18.
//  Copyright © 2018 dostuff. All rights reserved.
//

import UIKit
import CoreLocation

class Event: NSObject {
    
    var name: String?
    var eventDescription: String?
    var location: String?
    var time: String?
    var tags: [String]?
    var image: String?
    
    var distance: Double?
    var long: Double?
    var lat: Double?
    var decodedImage: UIImage?
    var locationOfEvent: CLLocationCoordinate2D?
    var daysTillDate: Int?
    var numberInDatabase: String!
    var rating: Int?
    
    init(nam: String, eventDescriptio: String, locatio: String, tim: String, tag: [String], imag: String ) {
        name = nam
        eventDescription = eventDescriptio
        location = locatio
        time = tim
        tags = tag
        image = imag
    }
}
