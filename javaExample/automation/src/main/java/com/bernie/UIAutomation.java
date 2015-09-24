package com.bernie;

import com.android.uiautomator.core.UiObject;
import com.android.uiautomator.core.UiObjectNotFoundException;
import com.android.uiautomator.core.UiSelector;

/**
 * Created by bida on 2015/9/22.
 */
public class UIAutomation {
    public static void main(String[] args) throws UiObjectNotFoundException {
        UiObject addNote = new UiObject(new UiSelector().text("add note"));
        addNote.getSelector();
        UiObject obj = new UiObject(new UiSelector().className("").textStartsWith(""));
        addNote.getFromParent(new UiSelector().index(1));
        new UiSelector().resourceId("android:id/title");
        new UiSelector().resourceIdMatches(".+id/title").childSelector(null);
//        obj.getFromParent()
        new UiSelector().focused(true).resourceId("");
    }
}
