---
id: TC-AC-SU-E2E-024-detail-user-header-general-info-dan-custom-field-accordion
title: "Detail User: Header read-only, hierarki badge User Type, General Information, dan Custom Field accordion"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-54
  - TC-AC-SU-55
  - TC-AC-SU-57
  - TC-AC-SU-58
  - TC-AC-SU-59
  - TC-AC-SU-60
  - TC-AC-SU-62
  - TC-AC-SU-63
coverage:
  web: automated
---

# Detail User: Header read-only, hierarki badge User Type, General Information, dan Custom Field accordion

## Prerequisites

- Login sebagai Role: Principal Total Control
- Terdapat data pengguna dengan Custom Field aktif, field Phone, dan tipe Temporary User

## Test Steps

### Screening Header Detail User dan Avatar Read-Only

1. Buka halaman Detail User untuk pengguna target
2. Verifikasi Header memuat: Avatar, Full Name, Status badge, Employee ID subtitle, dan switch Active
3. Hover kursor pada foto Avatar, verifikasi TIDAK ADA overlay tombol edit atau delete (foto murni read-only direfleksikan dari GS)
4. Verifikasi seluruh field General Information (Email, Position, Division) berstatus non-editable

### Hierarki Badge User Type dan Temporary Until

1. Amati badge User Type pada pengguna yang memiliki peran ganda Group Manager dan Admin
2. Verifikasi badge menampilkan `"Group Manager"` (mengikuti aturan prioritas top-down: Total Control > Read Only > Group Manager > Admin > Basic)
3. Amati field Temporary Until pada pengguna bertipe Temporary, verifikasi menampilkan teks format `"Temporary until [date]"`
4. Buka Detail User pada pengguna permanen, verifikasi field Temporary Until disembunyikan (hidden)

### Custom Field Accordion dan Render Field Phone

1. Amati section Custom Field pada halaman Detail User, verifikasi accordion dalam keadaan tertutup (collapsed by default)
2. Klik accordion Custom Field untuk membukanya
3. Verifikasi seluruh nilai Custom Field tampil secara read-only
4. Verifikasi field Phone tampil sebagai salah satu entri di dalam accordion Custom Field (bukan baris fixed General Info)

## Notes

- Informasi profil identitas di Detail User bersifat satu arah mencerminkan data master di Global Settings.
