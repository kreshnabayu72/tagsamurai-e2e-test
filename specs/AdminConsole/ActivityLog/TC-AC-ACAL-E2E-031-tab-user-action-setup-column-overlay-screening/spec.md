---
id: TC-AC-ACAL-E2E-031-tab-user-action-setup-column-overlay-screening
title: "Tab User Action — Screening Dropdown Overlay Quick Panel dan Popup Modal Setup Column 8 Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-174
  - TC-AC-ACAL-175
coverage:
  web: automated
---

# Tab User Action — Screening Dropdown Overlay Quick Panel dan Popup Modal Setup Column 8 Kolom

## Prerequisites

- Login sebagai Role: Principal Total Control
- Pengguna berada di `Admin Console > Activity Log` (Tab User Action)

## Test Steps

### Screening Quick Overlay Panel

1. Klik header kolom `⋯` pada tabel Tab User Action
2. Verifikasi overlay dropdown `"Column Visibility"` terbuka menampilkan 8 kolom dengan urutan default: `Date`, `Action`, `Object`, `Name`, `Field`, `Old Value`, `New Value`, `Modified By`
3. Verifikasi seluruh 8 kolom dalam kondisi tercentang (checked) dan aktif (enabled)
4. Verifikasi setiap baris pada dropdown memiliki drag handle

### Screening Popup Modal Setup Column 3 Zona

5. Klik menu `"Setup Column"` pada bagian bawah overlay
6. Verifikasi Popup Modal Setup Column terbuka dan memiliki 3 Zona dengan 8 baris kolom:
   - **Zona 1 (Header):** Judul `"Setup Column"`, deskripsi petunjuk, dan tombol close `(X)`
   - **Zona 2 (Body):** 8 baris daftar kolom dan panel Live Preview
   - **Zona 3 (Footer):** Tombol `[Reset to Default]`, `[Cancel]`, dan `[Save]`
7. Klik tombol `(X)` untuk menutup modal

## Notes

- Memverifikasi kepatuhan arsitektur Setup Column 2-level pada Tab User Action.
