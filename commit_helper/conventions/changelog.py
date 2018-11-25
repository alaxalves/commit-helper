def changelog_convention(tag, msg):
    tag = tag.upper()
    composed_message = "%s: %s\n" % (tag, msg)
    return composed_message


changelog_convention_help = \
    """
    Convention format:

    TAG: message
    ---
    Tag usage:

    ADD:


    """
