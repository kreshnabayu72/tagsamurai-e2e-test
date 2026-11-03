---
id: TC-AC-PF-E2E-040-masking-assigned-clients-total-control-read-only-account
title: Masking Assigned Clients - Total Control, Read Only Account-Wide, Dialog Cannot Archive Plan, Download, dan Navigasi Client Detail
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-104
  - TC-AC-PF-105
  - TC-AC-PF-107
  - TC-AC-PF-108
  - TC-AC-PF-109
coverage:
  web: automated
---

# Masking Assigned Clients - Total Control, Read Only Account-Wide, Dialog Cannot Archive Plan, Download, dan Navigasi Client Detail

## Prerequisites

- Mode: FE+BE
- Role yang diuji (akun aktor pertama login di hook `before`; akun lain lewat langkah Ganti akun eksplisit):

| Role | Akun | Email | Env password | Blok |
|---|---|---|---|---|
| Total Control (Principal) | #1 totalControlPrincipal | `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` | `AC_TC_PASSWORD` | langkah 1 sampai 9 |
| Read Only (Principal) | #2 readOnlyPrincipal | `readOnlyPrincipal_automated_{namaCompany}@qwertysystem.net` | `AC_PF_RO_PASSWORD` | langkah 10 sampai 14 |
| Group-Mix (Principal) | #8 groupMixPrincipal | `groupMixPrincipal_automated_{namaCompany}@qwertysystem.net` | `AC_PF_GM_PASSWORD` | langkah 15 sampai 34 |

- Login di hook `before` spec ini sebagai #1; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip mengikuti pernyataan di `suite.md` (hook suite menyetel flag true untuk akun aktor pre-setup).
- Data Pre-setup: Dataset Plan D (`Growth` v5 dengan 9 client termasuk PT Timur Jaya Zero Access, PT Bumi Sentosa Read Only, PT Wahana Nusantara CRUD), Dataset Plan G (`Paket Blok Mask` dipakai `PT Timur Jaya` Active Zero Access dan `PT Wahana Nusantara` Active CRUD). Spec hanya membaca data ini; nama literal tanpa suffix memakai pengecualian S-06/S-12 butir A-14 (nilai dirujuk lewat fixture data `fixtures/plans-licensing-plans-features.json` yang belum ada, ditandai di sini sesuai S-12).
- Kemampuan teknis: fixture backend (pemulihan Dataset Pre-setup, capability dan Group Role) disediakan tim FE/BE dan dinyatakan di `suite.md`; kemampuan membuka berkas CSV hasil unduhan (nama berkas, daftar client, header) untuk langkah 26 sampai 28.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

### Blok Total Control (Principal): TC-AC-PF-104

1. Buka Plan Detail `Growth` (klik Plan Name).
2. Klik Tab Assigned Clients.
3. Verifikasi seluruh Client Name berupa link aktif.
4. Buka Overlay Row Action pada `PT Timur Jaya`.
5. Verifikasi `Detail` dan `Push Update` aktif.
6. Buka Overlay Row Action pada `PT Bumi Sentosa`.
7. Verifikasi `Detail` dan `Push Update` aktif.
8. Buka Overlay Row Action pada `PT Wahana Nusantara`.
9. Verifikasi `Detail` dan `Push Update` aktif.

### Blok Read Only (Principal): TC-AC-PF-105

10. Ganti akun: logout, lalu login sebagai Read Only (Principal) (#2).
11. Buka Plan Detail `Growth` (klik Plan Name).
12. Klik Tab Assigned Clients.
13. Buka Overlay Row Action pada `PT Wahana Nusantara`.
14. Verifikasi Overlay Row Action hanya memuat `Detail`; `Push Update` Hidden.

### Blok Group-Mix (Principal): TC-AC-PF-107, TC-AC-PF-108, dan TC-AC-PF-109

15. Ganti akun: logout, lalu login sebagai Group-Mix (Principal) (#8).
16. Klik tab Custom.
17. Buka Overlay Row Action pada `Paket Blok Mask`.
18. Klik `Archive`.
19. Verifikasi dialog `Cannot Archive Plan` tampil dengan bullet • Paket Blok Mask, teks "This plan is currently assigned to 2 clients:", bullet • PT Timur Jaya dan • PT Wahana Nusantara (urut A-Z Client Name), teks "Reassign or archive those clients first.", dan tombol `[OK]`.
20. Klik `[OK]`.
21. Klik tab Default.
22. Buka Plan Detail `Growth` (klik Plan Name).
23. Klik Tab Assigned Clients.
24. Klik ikon Download.
25. Pilih `Download as CSV`.
26. Verifikasi berkas `Assigned-Clients-Growth` terunduh.
27. Verifikasi berkas memuat kesembilan client termasuk `PT Timur Jaya` (Zero Access) dan `PT Bumi Sentosa` (Read Only).
28. Verifikasi berkas tidak memuat kontrol aksi dan tidak memuat kolom Actions.
29. Klik link `PT Bumi Sentosa`.
30. Verifikasi link `PT Bumi Sentosa` membuka Client Detail dalam mode view-only.
31. Kembali ke Tab Assigned Clients lewat tombol Back browser.
32. Klik link `PT Wahana Nusantara`.
33. Verifikasi link `PT Wahana Nusantara` membuka Client Detail normal.
34. Verifikasi tab browser tetap yang sama (same-tab).

## Notes

- Spec ditulis per blok role karena tiap pergantian akun menuntut Step Ganti akun eksplisit (akun pertama login di hook `before`); langkah 10 dan 15 adalah Ganti akun eksplisit (S-07).
- Langkah penghubung (S-03): langkah 2, 12, 23 (membuka Tab Assigned Clients), langkah 16 dan 21 (pindah tab), langkah 20 (menutup dialog), langkah 31 (kembali ke Tab Assigned Clients).
- Langkah 19 menjalankan Expected dialog sebagai satu elemen karena TC menyebut judul, isi, dan tombolnya utuh dalam satu butir (S-01).
- Temuan untuk QA:
  - TC-AC-PF-107 precondition menyebut "aktor memiliki Delete" untuk aksi Archive, sedangkan Pre-setup #8 (`groupMixPrincipal`) menyebut Manage plans & licensing hanya Read dan Update, sehingga `Archive` Hidden bagi akun itu. Spec mengikuti TC (langkah 17 dan 18) dan hasilnya bergantung pada koreksi Pre-setup #8.
  - TC-AC-PF-105 precondition menyebut aktor Read Only juga memegang Group Role Manage active client CRUD pada group `PT Wahana Nusantara`, tetapi Pre-setup #2 tidak mencantumkan Group Role itu.
  - TC-AC-PF-108 Expected memuat isi berkas CSV (nama berkas, daftar client, header); spec memverifikasi nama berkas, jumlah dan nama baris client, dan ketiadaan kolom Actions, bukan isi sel lain.
  - Post Condition "Tidak ada perubahan data" dan "Plan tetap Active" tanpa langkah observasi tidak diasersi (S-01).
