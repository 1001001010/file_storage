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

    ⛓ Content: {content}
    """
    
    success_del = "🗑️Successfully deleted"
    adm_ed_price = "🖊️ Enter a new price"
    adm_ed_name = "🖊️ Enter a new name"
    adm_ed_content = "🖊️ Enter new content"
    buy_text = """Name: {name}
                  Price: {price}
                  
                  <b>Use the menu below to purchase</b>"""