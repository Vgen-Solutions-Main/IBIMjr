# Custom Domain Setup Guide

This guide explains how to configure your custom domain `jelvanricolcol.pro` on Namecheap to work with this GitHub Pages site.

## Prerequisites

- GitHub Pages is enabled for this repository
- You have access to your Namecheap account for `jelvanricolcol.pro`
- The `CNAME` file in this repository contains your domain name

## DNS Configuration on Namecheap

### Option 1: Using A Records (Recommended for Apex Domain)

1. Log in to your Namecheap account
2. Go to Domain List and click "Manage" for `jelvanricolcol.pro`
3. Go to "Advanced DNS" tab
4. Add the following A Records:

   | Type | Host | Value | TTL |
   |------|------|-------|-----|
   | A Record | @ | 185.199.108.153 | Automatic |
   | A Record | @ | 185.199.109.153 | Automatic |
   | A Record | @ | 185.199.110.153 | Automatic |
   | A Record | @ | 185.199.111.153 | Automatic |

5. Add a CNAME record for www subdomain (optional):

   | Type | Host | Value | TTL |
   |------|------|-------|-----|
   | CNAME Record | www | vgen-solutions-main.github.io. | Automatic |

### Option 2: Using CNAME Record (For Subdomain like www or ibim)

If you want to use a subdomain like `ibim.jelvanricolcol.pro`:

1. Update the `CNAME` file in this repository to contain: `ibim.jelvanricolcol.pro`
2. In Namecheap DNS settings, add:

   | Type | Host | Value | TTL |
   |------|------|-------|-----|
   | CNAME Record | ibim | vgen-solutions-main.github.io. | Automatic |

## Verification

1. After configuring DNS, wait for propagation (can take 5 minutes to 24 hours)
2. Check DNS propagation: https://dnschecker.org
3. Visit your domain: https://jelvanricolcol.pro
4. Verify the SVG displays correctly

## HTTPS/SSL

GitHub Pages automatically provisions an SSL certificate for your custom domain. This may take a few hours after DNS configuration.

## Troubleshooting

### SVG Not Showing

- Ensure the `CNAME` file exists in the repository root
- Verify DNS records are correctly configured
- Check that Jekyll build includes the SVG (see `_config.yml`)
- Clear browser cache and try again

### Domain Not Working

- Verify DNS records using: `dig jelvanricolcol.pro`
- Check GitHub Pages settings in repository settings
- Ensure HTTPS is enforced in GitHub Pages settings

### 404 Errors

- Ensure the `_config.yml` has correct `url` and `baseurl` settings
- Verify the GitHub Actions workflow completed successfully
- Check that all required files are committed to the repository

## BIMI Email Configuration

BIMI (Brand Indicators for Message Identification) allows your brand logo to be displayed in supported email clients when you send emails from your domain. This requires proper email authentication and DNS configuration.

### Prerequisites for BIMI

Before configuring BIMI, you must have these email authentication records in place:

1. **SPF (Sender Policy Framework)** - Authenticates which mail servers can send email on behalf of your domain
2. **DKIM (DomainKeys Identified Mail)** - Adds a digital signature to your emails
3. **DMARC (Domain-based Message Authentication, Reporting, and Conformance)** - Tells receiving servers how to handle emails that fail SPF/DKIM checks

### SPF Record Configuration

Add a TXT record for SPF to authorize mail servers:

| Type | Host | Value | TTL |
|------|------|-------|-----|
| TXT Record | @ | v=spf1 include:_spf.google.com ~all | Automatic |

*Note: Adjust the SPF record based on your email provider. Examples:*
- **Gmail/Google Workspace**: `v=spf1 include:_spf.google.com ~all`
- **Microsoft 365**: `v=spf1 include:spf.protection.outlook.com ~all`
- **SendGrid**: `v=spf1 include:sendgrid.net ~all`
- **Multiple providers**: `v=spf1 include:_spf.google.com include:sendgrid.net ~all`

### DKIM Record Configuration

DKIM records are provided by your email service provider. Contact your provider for the specific DKIM record to add.

Typical format:

| Type | Host | Value | TTL |
|------|------|-------|-----|
| TXT Record | [selector]._domainkey | v=DKIM1; k=rsa; p=[public-key] | Automatic |

*The [selector] and [public-key] values are provided by your email service.*

### DMARC Record Configuration

DMARC is required for BIMI. Add a TXT record with a DMARC policy:

| Type | Host | Value | TTL |
|------|------|-------|-----|
| TXT Record | _dmarc | v=DMARC1; p=quarantine; rua=mailto:dmarc@jelvanricolcol.pro; pct=100 | Automatic |

**DMARC Policy Options:**
- `p=none` - Monitor only (no enforcement)
- `p=quarantine` - Send suspicious emails to spam (recommended for BIMI)
- `p=reject` - Reject emails that fail authentication (strictest)

**Important for BIMI**: Your DMARC policy must be set to `quarantine` or `reject` (not `none`) for BIMI to work.

### BIMI Record Configuration

Once SPF, DKIM, and DMARC are properly configured, add the BIMI record:

| Type | Host | Value | TTL |
|------|------|-------|-----|
| TXT Record | default._bimi | v=BIMI1; l=https://jelvanricolcol.pro/IBIMjr.svg | Automatic |

**BIMI Record Explanation:**
- `v=BIMI1` - BIMI version
- `l=` - Location of your brand logo (must be SVG format, served over HTTPS)

**Logo Requirements:**
- Must be in SVG Tiny 1.2 or SVG Portable/Secure format
- Square aspect ratio (1:1) recommended
- Solid background color (transparent backgrounds may not work in all email clients)
- Maximum file size: 32 KB
- Served over HTTPS from your verified domain

### Verified Mark Certificate (VMC) - Optional

For enhanced BIMI support in more email clients, you may need a VMC from a certificate authority. This is required by some email providers like Gmail.

To add a VMC to your BIMI record:

```
v=BIMI1; l=https://jelvanricolcol.pro/IBIMjr.svg; a=https://jelvanricolcol.pro/vmc.pem
```

VMC providers include:
- DigiCert
- Entrust
- CSC

### Verification and Testing

After configuring all records:

1. **Verify DNS Propagation**: https://dnschecker.org
   - Check TXT records for `@`, `_dmarc`, and `default._bimi`

2. **Test SPF**: Use tools like MXToolbox SPF checker
   - https://mxtoolbox.com/spf.aspx

3. **Test DKIM**: Send a test email and check headers
   - Or use your email provider's DKIM verification tool

4. **Test DMARC**: https://mxtoolbox.com/dmarc.aspx
   - Verify DMARC policy is set to `quarantine` or `reject`

5. **Test BIMI**: 
   - https://bimigroup.org/bimi-generator/
   - Send test emails to BIMI-supported clients (Gmail, Yahoo, etc.)
   - It may take 24-48 hours for BIMI to appear after configuration

6. **Monitor DMARC Reports**: Check the email address specified in `rua=` for DMARC reports

### Troubleshooting BIMI

**Logo Not Appearing:**
- Ensure DMARC policy is `quarantine` or `reject` (not `none`)
- Verify SPF and DKIM authentication passes (99%+ pass rate required)
- Check SVG format compliance (use BIMI validator)
- Ensure logo is accessible via HTTPS
- Allow 24-48 hours for email clients to cache BIMI records

**DMARC Issues:**
- Verify SPF includes all mail servers sending on your behalf
- Ensure DKIM is properly configured with your email provider
- Check DMARC reports for authentication failures

**DNS Record Errors:**
- Use `dig TXT default._bimi.jelvanricolcol.pro` to verify BIMI record
- Use `dig TXT _dmarc.jelvanricolcol.pro` to verify DMARC record
- Ensure no typos in record values

## Files Involved

- `CNAME` - Contains your custom domain name
- `_config.yml` - Jekyll configuration with domain URL
- `.github/workflows/jekyll-gh-pages.yml` - GitHub Actions deployment workflow
- `IBIMjr.svg` - Brand logo used for BIMI display in emails

## Support

For DNS issues, contact Namecheap support: https://www.namecheap.com/support/
For GitHub Pages issues, check: https://docs.github.com/pages
For BIMI support, visit: https://bimigroup.org
