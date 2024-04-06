class Texts:
    ##################################                #####################################
    ##################################     Кнопки     #####################################
    ##################################                #####################################
    
    user_button = "📁 Resources"
    admin_button = "👨‍💻 Admin"

    back_adm_m = "🔙 Back"
    admin_menu_1 = "⛓ Resources"
    admin_menu_2 = "📩 Newsletter"
    
    ##################################                #####################################
    ##################################    Сообщения   #####################################
    ##################################                #####################################
    
    welcome = "🖐 Welcome"
    admin = "👨‍💻 Welcome to the admin panel"
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