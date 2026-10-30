---
id: TC-GS-ROLE-E2E-024-popup-assign-total-control-seleksi-counter-validasi-kosong-dan-cancel
title: "Popup Assign Total Control: Validasi Kosong, Selection Counter, Checkbox Header, dan Cancel"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-54
  - TC-GS-ROLE-55
  - TC-GS-ROLE-56
  - TC-GS-ROLE-57
coverage:
  web: automated
---

# Popup Assign Total Control: Validasi Kosong, Selection Counter, Checkbox Header, dan Cancel

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data: `[Assign]` hanya ditekan tanpa user terpilih (diblokir) dan popup ditutup dengan `[Cancel]`.
- Akun: Ahmad Fauzi (Total Control), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD` (Pre-setup #1). Login dan navigasi dilakukan sekali di hook `before`. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Data Pre-setup (hanya dibaca): kandidat picker Pre-setup #11, termasuk Sari Wulandari (Active) dan Maya Anggraini (Inactive), keduanya belum punya access level. Pool picker kurang dari 100 user dan lebih dari 10 user (Pre-setup #11 dan #18) sehingga dengan page size 100 keduanya berada di halaman aktif.
- N0: jumlah user ber-access level Total Control saat spec mulai, dibaca lewat kemampuan membaca jumlah user per access level yang disediakan tim FE/BE (bukan dari tabel yang hanya menampilkan satu halaman) dan dicatat di langkah 1; kemampuan yang sama dipakai untuk membaca jumlah di langkah 32.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Hook `beforeEach`: membuka Global Settings > Role & Permission > Tab Total Control.
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: membaca jumlah user per access level (N0); membaca posisi dan jarak elemen error terhadap tombol footer.

## Test Steps

### Persiapan

1. Catat N0, jumlah user ber-access level Total Control
2. Klik `[+ Assign]`
3. Ubah page size ke 100

### TC-GS-ROLE-54: Submit Assign Total Control tanpa memilih user

4. Klik `[Assign]` tanpa mencentang user
5. Verifikasi tidak ada toast
6. Verifikasi tidak ada dialog
7. Verifikasi teks error inline `You must pick a user`
8. Verifikasi teks error inline berseverity danger
9. Verifikasi teks error inline rata kanan, 4px di atas tombol footer
10. Verifikasi popup tetap terbuka

### TC-GS-ROLE-55: Selection counter Popup Assign Total Control

11. Centang Sari Wulandari
12. Verifikasi counter `1 user selected`
13. Centang Maya Anggraini
14. Verifikasi counter `2 users selected`
15. Hapus centang Maya Anggraini
16. Verifikasi counter `1 user selected`

### TC-GS-ROLE-56: Checkbox header Popup Assign memilih semua baris halaman aktif

17. Hapus centang Sari Wulandari
18. Centang checkbox header
19. Verifikasi counter sama dengan jumlah baris yang tampil di halaman aktif
20. Verifikasi semua baris halaman aktif checked
21. Hapus centang satu baris (baris pertama halaman aktif)
22. Verifikasi checkbox header tidak lagi checked penuh
23. Hapus centang checkbox header
24. Verifikasi baris pada halaman aktif masih tampil
25. Verifikasi semua baris halaman aktif unchecked

### TC-GS-ROLE-57: Cancel Popup Assign Total Control

26. Centang Sari Wulandari
27. Klik `[Cancel]`
28. Verifikasi tidak ada dialog
29. Verifikasi tidak ada toast
30. Verifikasi popup tertutup
31. Verifikasi Tab Total Control tampil
32. Verifikasi jumlah user ber-access level Total Control sama dengan N0
33. Ketik Search `Sari Wulandari`, tekan Enter
34. Verifikasi `No results found` tampil di Tab Total Control
35. Klik `(←)` pada kotak Search

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Mode: FE+BE.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Satu pembukaan popup dan satu penutupan (`[Cancel]`, langkah 27). Urutan: validasi diblokir (54), counter (55), checkbox header (56), lalu Cancel (57) yang menutup popup.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC sumber): langkah 1 (mencatat N0), langkah 3 (page size 100 supaya Sari Wulandari dan Maya Anggraini berada di halaman aktif), langkah 17 (menghapus centang sisa TC-GS-ROLE-55 supaya counter TC-GS-ROLE-56 hanya dari checkbox header), dan langkah 35 (menutup input Search).
- Langkah 5 dan 6 (absence state sementara) ditaruh segera setelah pemicu langkah 4 dan langkah 28 dan 29 segera setelah pemicu langkah 27 (bagian 8b butir 11).
- Langkah 31 (Tab Total Control tampil) adalah anchor positif bahwa layar di belakang popup termuat sebelum asersi jumlah dan Search; bukan butir Expected TC.
- Langkah 32 menjadi bukti "tidak ada user yang ter-assign" untuk TC-GS-ROLE-54 Expected c dan sekaligus mengamati TC-GS-ROLE-57 sesudah Cancel; langkah 34 (anchor positif: empty state `No results found` hasil Search) membuktikan Sari Wulandari tidak muncul di Tab Total Control.
- Pembagian TC lintas spec: TC-GS-ROLE-51, 52, 53, 77 ada di spec 023; TC-GS-ROLE-69 sampai 72 ada di spec 025; TC-GS-ROLE-73, 74 ada di spec 026; TC-GS-ROLE-75, 76, 293 ada di spec 027.
- Temuan untuk QA:
  - TC-GS-ROLE-55 dan 57 tidak menyebut halaman tempat Sari Wulandari dan Maya Anggraini berada; spec memakai page size 100 dengan asumsi pool kurang dari 100 user.
  - TC-GS-ROLE-56 langkah 4 ("Uncheck checkbox header") dilakukan saat header dalam keadaan tidak checked penuh (langkah 3); TC tidak menyatakan apakah klik pada keadaan itu menghapus semua centang atau memilih semua baris. Spec mengikuti Expected c (semua baris unchecked).
  - TC-GS-ROLE-54 Expected c ("tidak ada user yang ter-assign") tidak menyebut cara mengamati; spec memakai jumlah user Total Control dibanding N0 (langkah 32), dibaca lewat kemampuan yang disediakan tim FE/BE.
