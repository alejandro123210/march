
//
//  DetailViewController.swift
//  march
//
//  Created by Alejandro Gonzalez on 4/7/18.
//  Copyright © 2018 dostuff. All rights reserved.
//

import UIKit

class DetailViewController: UIViewController {
    
    @IBOutlet weak var imageView: UIImageView!
    @IBOutlet weak var textView: UITextView!
    var event: Event? 
    var button: UIButton?
    var slider: UISlider?
    var myView: UIView?
    var darkenView: UIView?
    
    var sliderRating: Int?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        textView.text = event!.eventDescription!
        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    @IBAction func ratingButton(_ sender: Any) {
        myView = UIView.init(frame: CGRect.init(x: 65, y: 300, width: 250, height: 100))
        myView!.backgroundColor = UIColor.white
        darkenView = UIView.init(frame: self.view.frame)
        darkenView!.backgroundColor = UIColor.black.withAlphaComponent(0.7)
        slider = UISlider.init(frame: CGRect.init(x: 25, y: 20, width: 200, height: 20))
        slider!.minimumValue = 0
        slider!.maximumValue = 5
        button = UIButton.init(frame: CGRect.init(x: 25, y: 65, width: 200, height: 20))
        button!.tintColor = UIColor.blue
        button!.setTitleColor(UIColor.blue, for: UIControlState.normal)
        button!.setTitleColor(UIColor.white, for: UIControlState.selected)
        button!.setTitle("Done", for: UIControlState.normal)
        button!.addTarget(self, action: #selector(Action), for: UIControlEvents.touchUpInside)
        myView!.addSubview(button!)
        myView!.addSubview(slider!)
        self.view.addSubview(darkenView!)
        self.view.addSubview(myView!)
    }
    
    @objc func Action(){
        print("tapped")
        sliderRating = Int(slider!.value)
        print(sliderRating!)
        event?.rating = sliderRating!
        button!.removeFromSuperview()
        slider!.removeFromSuperview()
        myView!.removeFromSuperview()
        darkenView!.removeFromSuperview()
        
    }
}
