//
//  File.swift
//  march
//
//  Created by Alejandro Gonzalez on 4/8/18.
//  Copyright © 2018 dostuff. All rights reserved.
//

import Foundation
class daUser: NSObject {
    
//    var gunControl: NSNumber!
//    var women: NSNumber!
//    var firstAmendment: NSNumber!
//    var proLife: NSNumber!
//    var bullying: NSNumber!
//    var politicalInstability: NSNumber!
//    var plannedParenthood: NSNumber!
//    var healthObesity: NSNumber!
//    var lgbtq: NSNumber!
//    var poverty: NSNumber!
//    var enviornment: NSNumber!
//    var waterSecurity: NSNumber!
//    var workingConditions: NSNumber!
//    var payIssues: NSNumber!
//    var alcohol: NSNumber!
//    var substanceIssues: NSNumber!
//    var largeScaleConflict: NSNumber!
//    var tax: NSNumber!
//    var finance: NSNumber!
//    var secondAmendment: NSNumber!
//    var proChoice: NSNumber!
    
    var tag_dictionary = [
        "gun control": 0,            "tax": 0,
        "women" : 0,            "finance" : 0,
        "first amendment" : 0,            "second amendment" : 0,
        "pro-life" : 0,            "pro-choice" : 0,
        "bullying" : 0,            "corruption" : 0,
        "political instability" : 0,            "climate change" : 0,
        "planned parenthood" : 0,            "medical" : 0,
        "health/obesity" : 0,            "animal rights/issues" : 0,
        "lgbtq" : 0,            "education" : 0,
        "poverty" : 0,            "antisemitism" : 0,
        "environment" : 0,            "food" : 0,
        "water security" : 0,            "racism" : 0,
        "working conditions" : 0,             "minimum wage" : 0,
        "pay issues" : 0,            "crime and justice system" : 0,
        "alcohol" : 0,            "drugs" : 0,
        "substance issues" : 0,            "terrorism" : 0,
        "large scale conflict" : 0,            "war" : 0
    ]
    
    override init() {
        
    }
    
//
//    func encode(with aCoder: NSCoder) {
//        aCoder.encode(tag_dictionary, forKey: "dict")
//    
//    }
//
//    required convenience init?(coder aDecoder: NSCoder) {
//        tag_dictionary = (aDecoder.decodeObject(forKey: "dict") as? [String : Int]
//    }
//
    
}
