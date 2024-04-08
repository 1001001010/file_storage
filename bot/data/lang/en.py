class Texts:
    ##################################                #####################################
    ##################################     Кнопки     #####################################
    ##################################                #####################################
    
    user_button = "📁 Resources"
    admin_button = "👨‍💻 Admin"

    back_adm_m = "🔙 Back"
    admin_menu_1 = "⛓ Resources"
    admin_menu_2 = "📩 Newsletter"
    
    adm_edit_pos1 = "💵 Price"
    adm_edit_pos2 = "👑 Title"
    adm_edit_pos3 = "🖊️ Content"
    adm_edit_pos4 = "❌ Delete"
    close = "❌ Close"
    only_text = "🖊️ Text"
    text_photo = "🖼️ Text with photo"
    admin_text_send = "🖊️ Enter your newsletter text"
    admin_photo_send = "🖼️ Send a photo for mailing"
    ##################################                #####################################
    ##################################    Сообщения   #####################################
    ##################################                #####################################
    
    welcome = "🖐 Welcome"
    admin = "👨‍💻 Welcome to the admin panel"
    user = "Available resource groups"
    admin_newsletter = "Send a message for newsletter"
    reg_user = "💎 New user {name} has been registered" # {name} - username of the user
    admin_list_resources = "📋 Available resource groups: "
    adm_group_name = "🖊️ Enter the name of the group: "
    adm_group_price = "💸 Specify the price for the group: "
    adm_group_content = "🌟 Specify content for the group: "
    adm_group_no_price = "You must specify a number"
    success_save = "Successfully saved"
    group_msg = """
    🆔 Id: <b>{id}</b>
    📝 Name: <b>{name}</b>
    💰 Price: <b>{price}₽</b>

    ⛓ Content: 
    {content}
    """
    
    success_del = "🗑️Successfully deleted"
    adm_ed_price = "🖊️ Enter a new price"
    adm_ed_name = "🖊️ Enter a new name"
    adm_ed_content = "🖊️ Enter new content"
    buy_text = """Name: {name}
                  Price: {price}
                  
                  <b>Use the menu below to purchase</b>"""
                  
    def refill_gen_text(self, way, amount, curr):
        message = f"""
    <b>⭐ Replenishment via: <code>{way}</code>
    💰 Amount: <code>{amount}{curr}</code>
    💎 To pay, click the button below:</b>
    """

        return(message)
    
    refill_link_inl = "💵 Go to cartoon"
    refill_check_inl = "💎 Check payment"
    
    Choose_crypto = "<b>⚙️ Select cryptocurrency:</b>"
    ne_oplat = "❌ Payment will not be found"
    
    def tovar(self, name, desc):
        msg = f"""
<b>Your product
Name: {name}

{desc}</b>
        """
        
    tip_newsletter = "Select newsletter type"