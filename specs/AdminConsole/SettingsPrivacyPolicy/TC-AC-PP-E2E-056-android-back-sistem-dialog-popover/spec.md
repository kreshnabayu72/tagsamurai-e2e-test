---
id: TC-AC-PP-E2E-056-android-back-sistem-dialog-popover
title: "Android: Back Sistem pada Modal, Dialog Publish Confirm, dan Popover Insert Link"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PP-189
  - TC-AC-PP-190
  - TC-AC-PP-191
coverage:
  mobile: automated
---

# Android: Back Sistem pada Modal, Dialog Publish Confirm, dan Popover Insert Link

## Prerequisites

- Mode: FE+BE. Platform: aplikasi native Android (PRD §4.6); tampilan berupa card list dan modal full-screen.
- Perangkat atau emulator Android dengan aplikasi native TAG Samurai Admin Console terpasang, serta kemampuan menekan tombol Back sistem dan mengetuk elemen UI.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`, `Spectra.env.AC_TC_PASSWORD`). Login di aplikasi Android dilakukan di hook `before`; hook `after` mengembalikan sesi ke akun default suite (akun yang sama).
- Hook `before`: Fixture BE men-seed Riwayat A (Version 3 Active, Version 2, Version 1). TC-AC-PP-190 mem-publish `Version 4`; karena TC-AC-PP-191 mengasumsikan `Version 3` Active, dataset dikembalikan ke Riwayat A lewat Fixture BE sebelum TC-AC-PP-191. Hook `after` mengembalikan dataset ke Riwayat A.
- Kemampuan teknis: `Spectra.intercept()` pada lalu lintas jaringan aplikasi Android untuk menahan respons Publish selama 5 detik (TC-AC-PP-190), dilepas kembali dalam langkah spec dan dipulihkan di hook `after` bila spec gagal di tengah; Fixture BE.
- Dokumen Privacy Policy bersifat tunggal platform-wide dan spec ini mem-publish `Version 4`, sehingga suite berjalan serial (`parallel: false`).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah spec).

## Test Steps

### TC-AC-PP-189: Back sistem pada Modal full-screen setara [✕] untuk state View dan state Edit

1. Buka Settings > Privacy Policy di aplikasi Android
2. Ketuk card `Version 3` sehingga Modal View terbuka
3. Tekan Back sistem
4. Verifikasi modal tertutup
5. Verifikasi tidak ada dialog yang tampil
6. Verifikasi daftar tampil
7. Ketuk `[⋯]` pada card `Version 3` lalu pilih `Edit`, tunggu konten termuat tanpa mengubah konten
8. Tekan Back sistem
9. Verifikasi modal tertutup
10. Verifikasi tidak ada dialog yang tampil (konten clean)
11. Ketuk `[⋯]` pada card `Version 3` lalu pilih `Edit`, tunggu konten termuat
12. Ketik " Android change." pada editor
13. Tekan Back sistem
14. Verifikasi Dialog "Unsaved Changes" tampil
15. Verifikasi Dialog "Unsaved Changes" memuat tombol `[Cancel]`
16. Verifikasi Dialog "Unsaved Changes" memuat tombol `[Leave]`
17. Ketuk `[Leave]`
18. Verifikasi modal tertutup
19. Verifikasi perubahan dibuang: daftar tetap menampilkan 3 card dan `Version 3` tetap Active tanpa `Version 4`

### TC-AC-PP-190: Back sistem saat dialog terbuka menutup dialog idle dan diblok saat Publishing

20. Ketuk `[⋯]` pada card `Version 3` lalu pilih `Edit`, tunggu konten termuat
21. Ketik " Android dialog." pada editor
22. Ketuk `[Publish New Version]` sehingga Dialog Publish Confirm tampil
23. Tekan Back sistem
24. Verifikasi dialog tertutup (setara `[Cancel]`)
25. Verifikasi modal Edit tetap terbuka
26. Verifikasi konten " Android dialog." dipertahankan di editor
27. Verifikasi tidak ada dialog bertumpuk
28. Atur intercept agar respons Publish ditahan 5 detik
29. Ketuk `[Publish New Version]`
30. Ketuk `[Publish]`
31. Tekan Back sistem selama Publishing
32. Verifikasi Back diblok
33. Verifikasi layar tidak berpindah
34. Verifikasi dialog tetap menampilkan `[Publish]` disabled
35. Lepas intercept sehingga respons Publish dilepaskan
36. Verifikasi Publish selesai dengan toast sukses "Success, Privacy Policy has been published."

### TC-AC-PP-191: Back sistem saat popover Insert Link terbuka hanya menutup popover

37. Kembalikan dataset ke Riwayat A lewat Fixture BE dan muat ulang Settings > Privacy Policy di aplikasi Android
38. Ketuk `[⋯]` pada card `Version 3` lalu pilih `Edit`, tunggu konten termuat
39. Ketik " Android link." di akhir konten editor
40. Ketuk tombol Link sehingga popover Insert Link terbuka
41. Tekan Back sistem
42. Verifikasi popover tertutup
43. Verifikasi tautan tidak disisipkan ke konten editor
44. Verifikasi modal tetap terbuka di state Edit
45. Verifikasi Dialog Unsaved Changes tidak tampil

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Spec Android: `coverage.mobile: automated` tanpa `coverage.web`. TC Android memakai TC universal; hanya aturan yang berbeda dari web (Back sistem) ditulis di spec ini (catatan TC: layout card list dan modal full-screen tidak dibuatkan TC terpisah).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung: langkah 37 (kembalikan dataset ke Riwayat A lewat Fixture BE karena TC-AC-PP-190 sudah mem-publish `Version 4`).
- Asersi atas TC: langkah 19 menerjemahkan Expected d TC-AC-PP-189 ("perubahan dibuang") menjadi pengamatan daftar (3 card, `Version 3` Active, tanpa `Version 4`), karena TC tidak memberi langkah observasi tambahan untuk membuktikan konten dibuang.
- Ukuran spec: 45 langkah (melewati sekitar 35) karena tiap klausa Expected menjadi satu `Verifikasi` (S-01). Spec tidak dipecah: ketiga blok TC mandiri (dataset di-reseed di awal blok lewat Fixture BE), satu kelas harness (aturan khusus Android), sehingga kegagalan satu blok tidak membuat blok berikutnya kehilangan makna.
- Temuan untuk QA:
  - TC-AC-PP-190 langkah 2 tidak menyatakan apakah konten " Android dialog." masih ada saat `[Publish New Version]` diketuk ulang; spec mengikuti Expected a (konten dipertahankan) sehingga konten sama dikirim pada Publish kedua.
  - Post Condition TC-AC-PP-190 ("Version 4 tersimpan satu kali") tidak punya langkah observasi sendiri dan tidak diasersi di luar Expected c.
  - Cara menahan respons Publish pada aplikasi native Android (proxy/intercept jaringan) tidak dijelaskan TC; dicatat sebagai kemampuan teknis di Prerequisites.
