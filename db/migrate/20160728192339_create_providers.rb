class CreateProviders < ActiveRecord::Migration[5.0]
  def change
    create_table :providers do |t|
      t.boolean :active

      t.timestamps
    end
  end
end
