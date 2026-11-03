---
id: TC-FA-RP-E2E-187-tabel-role-transaksi-tampilan-section-header-keterangan-2
title: "Tabel Role Transaksi: tampilan section, header, keterangan approver, dan state (2/3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1050
  - TC-FA-RP-1051
  - TC-FA-RP-1052
  - TC-FA-RP-1053
coverage:
  web: automated
---

# Tabel Role Transaksi: tampilan section, header, keterangan approver, dan state (2/3)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #18 (pohon group; node `IT Infrastructure`), #19 dan #40 (tabel Role Transaksi `IT Infrastructure` sub-tab `Disposal`: Asset Admin Nadia Putri, Ahmad Fauzi, Dimas Pranata; Monitoring & Report Oscar Pratama; Staff Putri Wulandari; Approver Pandu Wijaya). Tidak diubah spec ini kecuali penugasan Indra Kusuma di bawah.
- Pre-setup #17 (Indra Kusuma, tanpa Home Group; Active, Activated). Data Dinamis: penugasan Indra Kusuma sebagai Asset Admin pada `IT Infrastructure` sub-tab `Disposal` dibuat lewat sesi API aktor pada langkah 15 (precondition TC-FA-RP-1052, tidak diasersi) dan dicabut lewat sesi API aktor pada langkah 27; hook `after` mencabutnya bila masih ada.
- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun, nama pengguna, group, dan nilai kolom yang diasersi ditambahkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor (lihat `suite.md`) untuk menetapkan dan mencabut penugasan Role Transaksi; hover pada avatar.
- Pemulihan: preferensi Setup Column tabel yang disimpan spec ini dihapus di hook `after` (hapus preferensi kolom di browser, bukan `[Reset to Default]`; kemampuan disediakan tim FE); Pre-setup bersama tidak diubah kecuali dinyatakan di atas. Pemulihan ini belum terdaftar di `suite.md` (lihat Temuan untuk QA).

## Test Steps

### TC-FA-RP-1050: Urutan vertikal panel Transaction Role dan state default Accordion

1. Klik Tab `Transaction Role`
2. Klik sub-tab `Disposal`
3. Klik node `IT Infrastructure` di Sidebar Group Tree
4. Verifikasi urutan vertikal panel dari atas ke bawah: header section `Asset Admin`, `Monitoring & Report`, dan `Staff` dalam satu Accordion Multiple Expand, kartu `Approval Rule`, lalu header section `Approver` sebagai item Accordion tersendiri paling bawah
5. Verifikasi section `Asset Admin` terbuka
6. Verifikasi section `Monitoring & Report`, `Staff`, dan `Approver` tertutup
7. Verifikasi toolbar `Search | Filter | [+ Assign]` dan tabel hanya tampil di section yang terbuka
8. Verifikasi header section tidak memuat aksi

### TC-FA-RP-1051: Header section menampilkan jumlah assignment node terpilih

9. Verifikasi header `Asset Admin` memuat `3 users`
10. Verifikasi header `Monitoring & Report` memuat `1 user`
11. Verifikasi header `Staff` memuat `1 user`
12. Verifikasi header `Approver` memuat `1 user`
13. Klik node `Data Center`
14. Verifikasi keempat header memuat `0 users` (bentuk jamak untuk nol)

### TC-FA-RP-1052: Avatar stack tiga user pertama urut Name A-Z dengan +N dan hover nama lengkap

15. Lewat sesi API aktor, tetapkan Indra Kusuma sebagai Asset Admin pada `IT Infrastructure` sub-tab `Disposal` hingga tersimpan
16. Muat ulang halaman (F5) lalu buka kembali Tab `Transaction Role`, sub-tab `Disposal`, dan node `IT Infrastructure`
17. Verifikasi avatar stack pada header `Asset Admin` memuat tiga user pertama urut Name A-Z (Ahmad Fauzi, Dimas Pranata, Indra Kusuma)
18. Verifikasi avatar stack pada header `Asset Admin` memuat penanda `+1`
19. Arahkan kursor ke avatar Ahmad Fauzi
20. Verifikasi hover avatar menampilkan nama lengkap `Ahmad Fauzi`
21. Arahkan kursor ke avatar Dimas Pranata
22. Verifikasi hover avatar menampilkan nama lengkap `Dimas Pranata`
23. Arahkan kursor ke avatar Indra Kusuma
24. Verifikasi hover avatar menampilkan nama lengkap `Indra Kusuma`
25. Verifikasi header `Monitoring & Report` memuat satu avatar (Oscar Pratama)
26. Verifikasi header `Monitoring & Report` tanpa penanda `+N`
27. Lewat sesi API aktor, cabut penugasan Indra Kusuma sebagai Asset Admin pada `IT Infrastructure` sub-tab `Disposal` hingga tersimpan
28. Muat ulang halaman (F5) lalu buka kembali Tab `Transaction Role`, sub-tab `Disposal`, dan node `IT Infrastructure`

### TC-FA-RP-1053: Jumlah dan avatar header mencerminkan seluruh assignment node dan diperbarui seketika

29. Ketik Search `nadia` pada section `Asset Admin`, tekan Enter
30. Verifikasi tabel section `Asset Admin` tersaring satu baris (Nadia Putri)
31. Verifikasi header `Asset Admin` tetap `3 users`
32. Verifikasi header `Asset Admin` tetap memuat tiga avatar
33. Klik `(←)` pada kotak Search section `Asset Admin`
34. Klik `[+ Assign]` pada section `Asset Admin`
35. Centang Indra Kusuma pada popup, klik `[Assign]`
36. Verifikasi header `Asset Admin` berubah seketika menjadi `4 users` tanpa muat ulang halaman
37. Verifikasi avatar stack pada header `Asset Admin` memuat Indra Kusuma
38. Klik `[⋯]` pada baris Indra Kusuma, pilih `Remove`, klik `[Remove]`
39. Verifikasi header `Asset Admin` kembali `3 users`

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-1050, 1051, 1052, 1053). Seluruh TC berpost condition `-`; tidak ada asersi tambahan dari Post Condition.
- Langkah penghubung (tanpa awalan `Verifikasi`; dipakai untuk membuka konteks, menutup popup atau panel, membersihkan state, dan memulihkan kolom): langkah 1, 15, 16, 27, 28.
- Spec ini di atas 35 langkah (39 langkah nominal, sekitar 39 langkah setelah ekspansi iterasi). Alasan: seluruh blok satu kelas fungsional pada satu tabel dengan data Pre-setup yang sama, tiap TC berdiri sendiri dan state-nya dibersihkan sebelum TC berikutnya, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah yang membengkak adalah iterasi per kolom atau per kata kunci yang parameternya ada di tabel Prerequisites.
- Langkah pembuka TC-FA-RP-1050 mengandalkan state default Accordion pada kunjungan pertama ke Tab Transaction Role dalam spec ini; karena itu TC-FA-RP-1050 ditempatkan pertama.
- Temuan untuk QA:
  - TC-FA-RP-1052 menulis precondition "Indra Kusuma ditugaskan sebagai Asset Admin" tanpa menyebut cara; spec memakai sesi API aktor (S-04) dan mencabutnya sebelum TC-FA-RP-1053 yang menugaskan Indra Kusuma lewat UI.
  - TC tidak menyatakan posisi Tab, node, dan sub-tab setelah F5 pada Tab Transaction Role; spec menulis langkah penghubung yang membuka kembali Tab, node, dan sub-tab sebelum asersi lanjutan.
  - TC-FA-RP-1051 menyebut header `Approver` memuat `1 user` (Pandu Wijaya) sedangkan TC-FA-RP-1013 menyatakan Group Manager dan Total Control tidak tampil sebagai baris; spec mengasersi nilai header sesuai TC masing-masing.
