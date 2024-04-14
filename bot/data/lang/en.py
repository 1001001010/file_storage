class Texts:
    ################################## ################ ######################
    ################################## Buttons ############### ######################
    ################################## ################ ######################

    user_button = "📁 Resources"
    admin_button = "👨‍💻 Admin"

    back_adm_m = "🔙 Back"
    admin_menu_1 = "⛓ Resources"
    admin_menu_2 = "📩 Newsletter"

    oplata = "💳 Pay"

    adm_edit_pos1 = "💵 Price"
    adm_edit_pos2 = "👑 Title"
    adm_edit_pos3 = "🖊️ Content"
    adm_edit_pos5 = "📓 Description"
    adm_edit_pos4 = "❌ Delete"
    close = "❌ Close"
    only_text = "🖊️ Text"
    text_photo = "🖼️ Text with photo"
    admin_text_send = "🖊️ Enter your newsletter text"
    admin_photo_send = "🖼️ Send a photo for mailing"
    ################################## ################ ######################
    ################################## Messages ############### ######################
    ################################## ################ ######################

    welcome = "🖐 Welcome"
    admin = "👨‍💻 Welcome to the admin panel"
    user = "📃 Available resource groups: "
    admin_newsletter = "Send a message for newsletter"
    reg_user = "💎 New user {name} has been registered" # {name} - username of the user
    admin_list_resources = "📋 Available resource groups: "
    adm_group_name = "🖊️ Enter the name of the group: "
    adm_group_descr = "📓Specify the group description: "
    adm_group_price = "💸 Specify the price for the group: "
    adm_group_content = "🌟 Specify the content for the group: \nThe bot must be an administrator in the group and the ID must be correct!\n<b>Group ID must be separated by a new line\nFor example:\n-543534543\n-5345234\n-85435634</ b>"
    adm_group_no_price = "You must specify a number"
    success_save = "Successfully saved"
    choose_bank = "🔥 Select a Payment Method:"
    group_msg = """
    🆔 Id: <b>{id}</b>
    📝 Name: <b>{name}</b>
    💰 Price: <b>{price}₽</b>
    📓 Description: <b>{descr}</b>

    ⛓ Content:
    {content}
    """

    success_del = "🗑️Successfully deleted"
    adm_ed_price = "🖊️ Enter a new price"
    adm_ed_name = "🖊️ Enter a new name"
    adm_ed_content = "🖊️ Enter new content"
    adm_ed_descr = "🖊️ Enter a new description"
    buy_text = """🔒 Name: {name}
                💵 Price: {price} ₽
                📖 Description: {descr}"""
                
    def refill_gen_text(self, way, amount, curr):
        msg = f"""
<b>⭐ Replenishment via: <code>{way}</code>
💰 Amount: <code>{amount}{curr}</code>
💎 To pay, click on the button below:</b>
        """

        return(msg)

    refill_link_inl = "💵 Proceed to payment"
    refill_check_inl = "💎 Check payment"

    choose_crypto = "<b>⚙️ Select cryptocurrency:</b>"
    ne_oplat = "❌ Payment will not be found"

    def tovar(self, name, desc):
        msg = f"""
<b>Your product:
Name: {name}

{desc}</b>
        """

        return(msg)
    tip_newsletter = "Select newsletter type"