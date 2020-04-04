package com.example.chaquopyapp;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.TextView;
import android.widget.Toast;

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

public class MainActivity extends AppCompatActivity {

    TextView txt;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        txt = findViewById(R.id.txt);

        if (! Python.isStarted()) {
            Python.start(new AndroidPlatform(this));
        }

        try{
            Python py = Python.getInstance();
            PyObject pyf = py.getModule("hello");

            PyObject obj = pyf.callAttr("text");
            txt.setText(obj.toString());
        }
        catch (Exception e){
            Toast.makeText(this, e.toString(), Toast.LENGTH_SHORT).show();
        }


    }
}
