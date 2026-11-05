package studio.papercity;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;

public class PostcardActivity extends Activity {
    @Override
    public void onCreate(Bundle state) {
        super.onCreate(state);
        ScrollView scroll = new ScrollView(this);
        LinearLayout page = new LinearLayout(this);
        page.setOrientation(LinearLayout.VERTICAL);
        int margin = (int)(20 * getResources().getDisplayMetrics().density);
        page.setPadding(margin, margin, margin, margin);
        scroll.addView(page);
        setContentView(scroll);

        TextView title = new TextView(this);
        title.setText("Paper City at Dusk");
        title.setTextSize(30);
        page.addView(title);
        ImageView scene = new ImageView(this);
        scene.setImageResource(R.drawable.postcard);
        scene.setContentDescription("A footbridge leads to three folded-paper towers.");
        scene.setAdjustViewBounds(true);
        page.addView(scene);
        Button toggle = new Button(this);
        page.addView(toggle);
        TextView label = new TextView(this);
        label.setText("MOTH-27 · From the Lantern Gate, cross the bridge to the three towers.");
        label.setTextSize(20);
        page.addView(label);
        boolean visible = state != null && state.getBoolean("labelOpen");
        label.setVisibility(visible ? View.VISIBLE : View.GONE);
        toggle.setText(visible ? "Hide wall label" : "Read wall label");
        toggle.setOnClickListener(view -> {
            boolean open = label.getVisibility() == View.GONE;
            label.setVisibility(open ? View.VISIBLE : View.GONE);
            toggle.setText(open ? "Hide wall label" : "Read wall label");
        });
        this.label = label;
    }
    private TextView label;
    @Override
    protected void onSaveInstanceState(Bundle state) {
        super.onSaveInstanceState(state);
        state.putBoolean("labelOpen", label.getVisibility() == View.VISIBLE);
    }
}
