---
id: TC-AC-SU-E2E-028-detail-user-header-readonly-badge-user-type-dan-general-info
title: "Detail User: Header Read-Only, Avatar, Badge User Type, dan General Information"
priority: High
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

# Detail User: Header Read-Only, Avatar, Badge User Type, dan General Information

## Prerequisites

- Login sebagai Total Control
- Terdapat pengguna dengan profil lengkap dan kustomisasi field

## Test Steps

### Screening Header Detail User
1. Buka `Admin Console > Settings > User`
2. Klik nama user target pada tabel untuk membuka halaman `Detail User`
3. Verifikasi breadcrumb menampilkan: `"Settings > User > [Full Name]"`
4. Verifikasi header memuat: Avatar foto profil, teks Full Name, teks Email, badge status Active/Inactive, dan badge `User Type`
5. Verifikasi badge User Type menampilkan nilai yang sesuai (misal: `Employee`, `External`, atau `Contractor`)

### Screening Seksi General Information dan Custom Field
6. Verifikasi seksi General Information menampilkan data read-only: `Phone Number`, `Position`, `Division`, dan `Last Updated`
7. Verifikasi format tanggal `Last Updated` mematuhi konfigurasi General Settings
8. Klik accordion `Custom Field`
9. Verifikasi seluruh label dan nilai custom field ter-render dengan benar dalam format read-only

## Notes

Memastikan seluruh informasi identitas pengguna tersaji akurat di halaman detail.
