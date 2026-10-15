---
id: TC-AC-PP-E2E-028-defense-konten-kosong-ditolak-server
title: "Defense-in-Depth: Server Menolak Konten Kosong, Konten Hanya Sanitasi, dan Konten &nbsp; pada Publish"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PP-85
  - TC-AC-PP-86
  - TC-AC-PP-87
coverage:
  web: automated
---

# Defense-in-Depth: Server Menolak Konten Kosong, Konten Hanya Sanitasi, dan Konten &nbsp; pada Publish

## Prerequisites

- Mode: FE+BE. Kelas harness a (defense-in-depth): `Spectra.intercept()` dipakai di atas backend nyata untuk mengganti body permintaan Publish sehingga validasi client terlewati dan penolakan server (422) teramati; intercept dilepas segera setelah permintaan Publish terkirim dan dipulihkan di hook `after` bila spec gagal di tengah.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Hook `before` login akun ini dan membuka Settings > Privacy Policy; hook `after` mengembalikan sesi ke akun default suite yang sama (Total Control). Nama env `AC_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Dataset: Riwayat A (Version 3 Active diterbitkan `John Doe` 10 Aug 2026 20:30 UTC dengan H1 `Privacy Policy`, paragraf `This Privacy Policy describes how we collect, use, and protect your information.`, H3 `1. Information We Collect`; Version 2 `John Doe` 02 Jul 2026; Version 1 `Jane Smith` 15 Jan 2026, akun sudah dihapus). Hook `before` men-seed Riwayat A lewat Fixture BE (riwayat versi append-only dan tidak dapat dihapus lewat UI); hook `after` mengembalikan dataset ke Riwayat A. Spec ini tidak membuat versi baru karena server menolak ketiga permintaan.
- Dokumen Privacy Policy bersifat tunggal platform-wide; suite berjalan serial (`parallel: false`).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah spec ini).
- Kemampuan teknis: `Spectra.intercept()` untuk mengganti body Publish dengan (a) konten kosong `""`, (b) `<script>alert(1)</script>`, (c) `<p>&nbsp;</p>`; deteksi dialog `alert` browser (harus tidak muncul).

## Test Steps

### TC-AC-PP-85: Server menolak konten kosong yang lolos validasi client dengan error inline V-01 tanpa toast

1. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
2. Tunggu konten editor termuat
3. Ketik " Server check." di akhir konten
4. Klik `[Publish New Version]`
5. Atur intercept agar body permintaan Publish diganti dengan konten kosong (`""`)
6. Klik `[Publish]`
7. Lepas intercept body Publish
8. Verifikasi server menolak dengan status 422
9. Verifikasi error inline "Privacy Policy content must not be empty" tampil di bawah editor
10. Verifikasi Dialog Publish Confirm tertutup
11. Verifikasi Modal tetap di state Edit
12. Verifikasi konten editor dipertahankan
13. Verifikasi tidak ada toast yang tampil

### TC-AC-PP-86: Konten yang kosong setelah sanitasi ditolak server dengan error inline V-01 dan tanpa versi serta log

14. Ketik " Sanitize check." di akhir konten
15. Klik `[Publish New Version]`
16. Atur intercept agar body permintaan Publish diganti dengan `<script>alert(1)</script>`
17. Klik `[Publish]`
18. Lepas intercept body Publish
19. Verifikasi error inline "Privacy Policy content must not be empty" tampil di bawah editor
20. Verifikasi tidak ada toast yang tampil
21. Verifikasi Dialog Publish Confirm tertutup
22. Verifikasi Modal tetap di state Edit
23. Verifikasi tidak ada dialog alert dari browser

### TC-AC-PP-87: Konten hanya `&nbsp;` atau spasi yang dikirim langsung ke server

24. Ketik " NBSP check." di akhir konten
25. Klik `[Publish New Version]`
26. Atur intercept agar body permintaan Publish diganti dengan `<p>&nbsp;</p>`
27. Klik `[Publish]`
28. Lepas intercept body Publish
29. Verifikasi server menolak dengan status 422
30. Verifikasi error inline "Privacy Policy content must not be empty" tampil di bawah editor
31. Verifikasi Dialog Publish Confirm tertutup
32. Verifikasi Modal tetap di state Edit
33. Verifikasi konten editor dipertahankan
34. Verifikasi tidak ada toast yang tampil
35. Klik `✕` di header
36. Verifikasi Dialog "Unsaved Changes" tampil
37. Klik `[Leave]`
38. Verifikasi tabel menampilkan 3 baris Riwayat A
39. Verifikasi tidak ada `Version 4`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`. Kelas harness a (defense-in-depth).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC mengikuti urutan nomor. Ketiga TC berbagi satu sesi modal Edit (satu kali buka, satu kali menutup di langkah 35-37) karena setelah penolakan server modal tetap terbuka di state Edit dengan konten dipertahankan; langkah 1-2 TC-AC-PP-86 dan TC-AC-PP-87 ("Edit, tunggu konten termuat") dipenuhi sesi yang sama dan hanya langkah mengetik (langkah 14, 24) serta `[Publish New Version]` yang diulang.
- Langkah penghubung (tanpa awalan Verifikasi): langkah 7, 18, 28 (melepas intercept body Publish setelah permintaan terkirim, S-09), langkah 35-37 (menutup modal dirty lewat `✕` lalu `[Leave]`; dialog diverifikasi di langkah 36 sebagai asersi tambahan untuk deterministik S-08).
- Asersi tambahan yang dicatat: langkah 38-39 mengamati tabel setelah modal ditutup untuk memenuhi Expected d TC-AC-PP-85 dan TC-AC-PP-87 ("Tidak ada versi baru"); TC-AC-PP-86 tidak punya Expected "tidak ada versi baru", sehingga amatan itu berlaku untuk ketiganya sekaligus.
- Jumlah langkah (39) sedikit melewati sekitar 35 langkah karena satu `Verifikasi` per klausa Expected (S-01) pada tiga TC satu topik dan satu kelas harness (a) yang berbagi satu sesi modal Edit; tiap blok `###` tetap bermakna walau blok sebelumnya gagal (soft assertion) kecuali kegagalan keras membuka modal Edit, sehingga spec tidak dipecah.
- Post Condition TC ("Tidak ada versi baru dan tidak ada record audit") tanpa langkah observasi di TC tidak diasersi; asersi absence log milik spec log (TC-AC-PP-159).
- Temuan untuk QA:
  - TC-AC-PP-86 Expected tidak menyebut status HTTP penolakan (hanya error inline); spec tidak mengasersi status. TC-AC-PP-85 dan TC-AC-PP-87 menyebut 422.
  - TC-AC-PP-86 Expected c "Tidak ada dialog alert dari browser" membutuhkan deteksi dialog `alert` di runner; kemampuan ini dituliskan di Prerequisites.
