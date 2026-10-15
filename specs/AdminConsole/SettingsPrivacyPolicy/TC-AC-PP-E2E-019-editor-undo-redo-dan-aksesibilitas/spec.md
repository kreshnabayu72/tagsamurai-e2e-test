---
id: TC-AC-PP-E2E-019-editor-undo-redo-dan-aksesibilitas
title: "Editor: Undo dan Redo serta Aksesibilitas Area Editor dan Toolbar"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PP-52
  - TC-AC-PP-53
coverage:
  web: automated
---

# Editor: Undo dan Redo serta Aksesibilitas Area Editor dan Toolbar

## Prerequisites

- Mode: mock.
- Kebutuhan mock (dijalankan tim FE sebagai integration test, tanpa backend nyata): respons endpoint daftar riwayat versi dengan dataset Riwayat A (Version 3 Active/John Doe, Version 2, Version 1) dan respons endpoint konten versi Active (Version 3: H1 `Privacy Policy`, paragraf `This Privacy Policy describes how we collect, use, and protect your information.`, H3 `1. Information We Collect`). Payload sesi dan izin Total Control (capability "Manage privacy policy" Read dan Update) agar row action `Edit` tampil pada baris `Version 3`. Tidak ada endpoint Publish yang dipanggil.
- Akun: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, Andi Wijaya, env `Spectra.env.AC_TC_PASSWORD`); login nyata dengan `AC_TC_PASSWORD` di hook `before` hanya untuk run non-mock, pada run mock sesi disediakan harness lewat payload sesi dan izin di atas; hook `after` mengembalikan sesi ke akun default suite yang sama. Tidak ada state backend yang diubah sehingga tidak ada pemulihan dataset.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah).

## Test Steps

### TC-AC-PP-52: Tombol Undo dan Redo pada toolbar editor membatalkan dan mengulang perubahan teks

1. Buka Settings > Privacy Policy
2. Klik `[⋯]` pada baris `Version 3`
3. Pilih `Edit`
4. Tunggu konten termuat
5. Klik di akhir konten
6. Ketik " Added sentence."
7. Verifikasi konten editor memuat " Added sentence." di akhir konten
8. Klik Undo
9. Verifikasi " Added sentence." hilang
10. Verifikasi konten kembali identik dengan konten awal Version 3
11. Klik Redo
12. Verifikasi " Added sentence." muncul kembali di akhir konten
13. Verifikasi modal tetap di state Edit
14. Verifikasi tidak ada dialog pada seluruh langkah 5 sampai 12
15. Klik `[✕]` pada header modal
16. Verifikasi Dialog "Unsaved Changes" tampil
17. Klik `[Leave]`

### TC-AC-PP-53: Accessibility editor: role dan label ARIA pada area editor dan tombol toolbar yang disebut PRD

18. Klik `[⋯]` pada baris `Version 3`
19. Pilih `Edit`
20. Tunggu konten termuat
21. Periksa atribut area editor
22. Verifikasi area editor memiliki `role="textbox"`
23. Verifikasi area editor memiliki `aria-multiline="true"`
24. Periksa atribut seluruh tombol pada toolbar
25. Verifikasi tombol toolbar memiliki `aria-label` berurutan: "Heading 1", "Heading 2", "Heading 3", "Bold", "Italic", "Underline", "Bulleted list", "Numbered list", "Insert link", "Undo", "Redo"
26. Verifikasi tombol Bold memiliki `aria-label` "Bold"
27. Verifikasi tombol Link memiliki `aria-label` "Insert link"
28. Tekan Tab berulang kali dari area editor
29. Verifikasi fokus keyboard berputar di dalam modal (focus trapped)
30. Verifikasi fokus keyboard tidak keluar ke elemen di belakang modal
31. Klik `[✕]` pada header modal
32. Tunggu modal tertutup

## Notes

- Mode: mock (seluruh API di-mock; kedua TC bertanda FE Test "UI Only"). Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung: langkah 15-17 menutup modal Edit yang dirty lewat `✕`, dialog `Unsaved Changes`, lalu `[Leave]` (S-08); langkah 31 menutup modal yang bersih dan langkah 32 hanya menunggu modal tertutup sebagai langkah penghubung tanpa `Verifikasi` (penutupan bersih tanpa dialog tidak ada di Expected TC-AC-PP-53). Dialog `Unsaved Changes` pada langkah 16 adalah bagian penutupan deterministik, bukan asersi TC-AC-PP-52.
- Pemakaian TC-AC-PP-53 langkah 1 TC ("Klik `[⋯]` ... Edit") disalin utuh sebagai langkah 18-20 karena TC-AC-PP-53 berdiri sendiri dan tidak menumpang state TC-AC-PP-52 (S-04).
- Temuan untuk QA: (1) TC-AC-PP-52 Expected d ("tidak ada dialog pada seluruh langkah") tidak menyebut kapan diasersi; spec mengasersinya sekali setelah Redo untuk rentang langkah 5-12. (2) TC-AC-PP-53 langkah 4 ("Tekan Tab berulang kali") tidak menyebut jumlah tekanan; tim FE menentukan jumlah yang cukup melewati semua kontrol fokusable di modal sehingga perputaran terlihat. (3) Post Condition kedua TC ("Tidak ada perubahan data") tidak punya langkah observasi sehingga tidak diasersi.
