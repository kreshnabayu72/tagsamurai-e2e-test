---
id: TC-FA-GRP-E2E-014-android-guided-tooltip-drawer-dan-group-context-header-aktor-scoped
title: "Android: Guided Tooltip Membuka Drawer Otomatis, Group Context Header di Atas Toolbar, dan [+] Group Hanya Total Control/Default User"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-971
  - TC-FA-GRP-985
coverage:
  mobile: automated
---

# Android: Guided Tooltip Membuka Drawer Otomatis, Group Context Header di Atas Toolbar, dan [+] Group Hanya Total Control/Default User

## Prerequisites

- Mode: FE+BE.
- Perangkat: perangkat atau emulator Android dengan aplikasi Fixed Asset terpasang, disediakan tim FE. Perangkat dipakai bersama sehingga spec ini berjalan serial (`parallel: false`). Spec ini tidak memakai hook web suite: login ke aplikasi dilakukan di langkah.
- Akun aktor pertama: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Akun aktor kedua: Group Manager scope Region West (Pre-setup No 4) `groupManagerGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GM_PASSWORD`.
- Flag Guided Tooltip `fa-settings-groups`: kemampuan menyetel flag menjadi belum diset atau `seen` per akun disediakan tim FE/BE. Flag akun Total Control disetel belum diset oleh langkah 1 dan menjadi `seen` oleh langkah 9; flag akun Group Manager disetel `seen` sebelum spec berjalan dan keduanya dipulihkan ke nilai awal setelah spec selesai.
- Data Pre-setup (hanya dibaca): pohon group baku Tabel A (Pre-setup No 9) dengan Head Office.
- Kemampuan teknis: fixture BE dan sesi API aktor, disediakan tim FE/BE.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global selain flag Guided Tooltip yang dipulihkan.

## Test Steps

### TC-FA-GRP-971: Guided Tooltip Android membuka drawer tertutup otomatis

1. Setel flag `fa-settings-groups` akun Total Control menjadi belum diset
2. Login ke aplikasi Android sebagai Total Control
3. Tutup drawer sidebar
4. Buka halaman Groups
5. Verifikasi drawer dibuka otomatis selama Step 1 (Sidebar Group Tree)
6. Verifikasi Step 1 tidak dilewati dan penomor tetap `Step 1 of 3`
7. Klik [Next]
8. Klik [Next]
9. Klik [Done]
10. Verifikasi drawer kembali tertutup
11. Buka ulang halaman Groups
12. Verifikasi drawer tetap tertutup (state persisten tidak berubah)

### TC-FA-GRP-985: Group Context Header di atas Toolbar dan [+] Group di header drawer

13. Buka drawer sidebar
14. Pilih Head Office pada drawer
15. Verifikasi Group Context Header tampil di atas Toolbar dan Card List
16. Verifikasi Group Context Header memuat satu judul `Head Office` dengan metrik berlabel `Total Asset: [N]` dan `Total User: [N]`
17. Buka drawer sidebar
18. Verifikasi [+] Group berada di header drawer sidebar untuk Total Control
19. Logout dari aplikasi Android
20. Login ke aplikasi Android sebagai Group Manager scope Region West
21. Buka halaman Groups
22. Buka drawer sidebar
23. Verifikasi drawer sidebar terbuka dengan tree group tampil (anchor permukaan)
24. Verifikasi Group Manager tidak melihat [+] Group di header drawer

## Notes

- Langkah penghubung (S-03): langkah 3 (menyiapkan drawer tertutup), langkah 11 (membuka ulang halaman untuk mengamati state persisten), langkah 13 dan 14 (membuka drawer dan memilih Head Office untuk TC-FA-GRP-985), langkah 17 (membuka drawer untuk mengamati header drawer), langkah 19 sampai 22 (ganti akun eksplisit ke Group Manager).
- Urutan TC dalam spec: 971, 985 (TC-FA-GRP-971 lebih dulu karena membutuhkan flag belum diset; langkah 9 menyetel flag `seen`).
- Temuan untuk QA:
  - Precondition TC-FA-GRP-985 menyebut "akun Total Control dan akun Group Manager (scope Region West) tersedia" tanpa email; email diambil dari Pre-setup No 1 dan No 4. Langkah 5 mengasersi drawer terbuka tanpa menyebut elemen drawer yang dicek selain header.
  - Tidak ada TC Android untuk Role Matrix [+] Group bagi Default User; judul spec menyebut Total Control/Default User sesuai Expected, sedangkan spec hanya menguji Total Control dan Group Manager sesuai langkah TC.
  - Langkah 23 adalah `Verifikasi` tambahan sebagai anchor positif absence [+] Group (8b butir 2) dan tidak ada di Expected TC.
