package com.bernie.hessiantry;

import java.io.Serializable;

/**
 * Created by bida on 2015/8/5.
 */
public class MyCar implements Serializable{
    private static final long serialVersionUID = 4736905401908455439L;
    private String carName;
    private String carModel;

    public String getCarName() {
        return carName;
    }

    public void setCarName(String carName) {
        this.carName = carName;
    }

    public String getCarModel() {
        return carModel;
    }

    public void setCarModel(String carModel) {
        this.carModel = carModel;
    }

    @Override
    public String toString(){
        return "my car name : [" + this.carName + "],model : " + this.carModel + "]";
    }
}
