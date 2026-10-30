---
id: TC-GS-DIV-E2E-047-setup-column-tabel-screening-hide-unhide-cancel-dan-kolom-terakhir
title: "Setup Column Tabel Division: Screening, Hide/Unhide, Tutup Tanpa Simpan, dan Kolom Visible Terakhir"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-171
  - TC-GS-DIV-172
  - TC-GS-DIV-173
  - TC-GS-DIV-177
  - TC-GS-DIV-178
coverage:
  web: automated
---

# Setup Column Tabel Division: Screening, Hide/Unhide, Tutup Tanpa Simpan, dan Kolom Visible Terakhir

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Division.
- Akun: Total Control, `Sari Dewi (Sari D)`, `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > User > Division dilakukan sekali di hook `before` (seedSession). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Data Pre-setup (tetap di environment, hanya dibaca): Finance (FIN), Human Resources (HR), Legal (LGL), Operations (OPS), Compliance (CMP), Treasury (TRS). Asersi spec ini hanya menyangkut kolom tabel, bukan kumpulan nama atau jumlah baris, sehingga Population D-02 tidak di-seed; tabel memuat baris sesuai state environment.
- Data uji: kolom `Name`, `Code`, `Last Updated` (semua Hideable, default visible).
- Preferensi kolom (visibilitas, urutan, pin) tersimpan per user di browser per tabel dan menjadi permanen setelah `[Save]` (PRD division.md §4.2e; prd-conventions.md §9.3); "muat ulang halaman" dilakukan pada konteks browser yang sama supaya penyimpanan browser tetap ada.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State yang diubah dan dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): konfigurasi kolom tabel Division dikembalikan ke default (Name, Code, Last Updated tampil berurutan, tanpa pin) lewat `[Reset to Default]` atau penghapusan preferensi kolom tabel Division di browser.
- Hook `beforeEach`: kembali ke layar Global Settings > User > Division.
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: mengarahkan kursor ke checkbox disabled untuk membaca tooltip; menekan Esc pada modal; membaca dan menghapus preferensi kolom di penyimpanan browser.

## Test Steps

### TC-GS-DIV-171: Screening Overlay Column Visibility tabel Division

1. Klik header kolom Actions (⋯)
2. Verifikasi overlay tampil tanpa backdrop
3. Verifikasi daftar kolom berurutan `Name`, `Code`, `Last Updated`
4. Verifikasi masing-masing kolom tercentang
5. Verifikasi checkbox tiap kolom enabled
6. Verifikasi masing-masing kolom memiliki drag handle
7. Verifikasi item `Setup Column...` di bagian bawah overlay

### TC-GS-DIV-172: Screening Popup Setup Column tabel Division

8. Klik item `Setup Column...`
9. Verifikasi Header: Title `Setup Column`
10. Verifikasi Header: Subtitle `Manage column visibility, reorder, and freeze columns.`
11. Verifikasi Header: icon close `[✕]`
12. Verifikasi Body: Search input `Search column name...`
13. Verifikasi Body: daftar kolom `Name`, `Code`, `Last Updated` masing-masing tercentang
14. Verifikasi Body: drag handle `⠿` pada tiap kolom
15. Verifikasi Body: icon pin pada tiap kolom
16. Verifikasi Body: preview tabel merefleksikan susunan kolom
17. Verifikasi Footer: tombol `[Reset to Default]` (text, primary)
18. Verifikasi Footer: tombol `[Save]` (filled, success)

### TC-GS-DIV-173: Setup Column: hide dan unhide tiap kolom lewat popup lalu Save

19. Hilangkan centang `Name` (kolom lain tetap tercentang)
20. Klik `[Save]`
21. Verifikasi kolom `Name` tidak tampil di tabel
22. Buka kembali Popup Setup Column lewat header Actions (⋯) lalu `Setup Column...`
23. Centang kembali `Name`
24. Klik `[Save]`
25. Verifikasi kolom `Name` tampil kembali di tabel
26. Buka Popup Setup Column lewat header Actions (⋯) lalu `Setup Column...`
27. Hilangkan centang `Code` (kolom lain tetap tercentang)
28. Klik `[Save]`
29. Verifikasi kolom `Code` tidak tampil di tabel
30. Buka kembali Popup Setup Column lewat header Actions (⋯) lalu `Setup Column...`
31. Centang kembali `Code`
32. Klik `[Save]`
33. Verifikasi kolom `Code` tampil kembali di tabel
34. Buka Popup Setup Column lewat header Actions (⋯) lalu `Setup Column...`
35. Hilangkan centang `Last Updated` (kolom lain tetap tercentang)
36. Klik `[Save]`
37. Verifikasi kolom `Last Updated` tidak tampil di tabel
38. Buka kembali Popup Setup Column lewat header Actions (⋯) lalu `Setup Column...`
39. Centang kembali `Last Updated`
40. Klik `[Save]`
41. Verifikasi kolom `Last Updated` tampil kembali di tabel
42. Muat ulang halaman (F5)
43. Verifikasi konfigurasi terakhir tetap tersimpan: kolom `Name`, `Code`, `Last Updated` tampil

### TC-GS-DIV-177: Setup Column: X dan Esc membuang perubahan preview

44. Buka Popup Setup Column lewat header Actions (⋯) lalu `Setup Column...`
45. Hilangkan centang `Code`
46. Klik `[✕]`
47. Verifikasi tabel kembali memakai konfigurasi tersimpan terakhir (kolom `Code` tampil) setelah ditutup lewat `[✕]`
48. Buka kembali Popup Setup Column lewat header Actions (⋯) lalu `Setup Column...`
49. Hilangkan centang `Code`
50. Tekan tombol Esc
51. Verifikasi tabel kembali memakai konfigurasi tersimpan terakhir (kolom `Code` tampil) setelah ditutup lewat Esc

### TC-GS-DIV-178: Setup Column: kolom visible terakhir tidak dapat di-uncheck

52. Buka Popup Setup Column lewat header Actions (⋯) lalu `Setup Column...`
53. Hilangkan centang `Code`
54. Hilangkan centang `Last Updated`
55. Arahkan kursor ke checkbox `Name`
56. Verifikasi checkbox `Name` disabled dan tidak dapat di-uncheck
57. Verifikasi tooltip `At least one column must remain visible.`
58. Klik `[✕]` untuk menutup popup tanpa Save

## Notes

- Sumber TC: `global-settings/division/TestCases/tc-division.md`. Mode: FE+BE (preferensi kolom disimpan di browser; tabel dimuat dari backend nyata).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (171, 172, 173, 177, 178) dipertahankan; dua TC screening (171, 172) di awal sebelum aksi yang mengubah konfigurasi kolom.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 58 (menutup popup tanpa Save agar perubahan checkbox pada langkah 53 dan 54 tidak tersimpan; hook `after` sebagai cadangan). Langkah 19 memakai popup yang masih terbuka dari TC-GS-DIV-172, sehingga langkah 1 TC-GS-DIV-173 ("Buka Popup Setup Column") dipenuhi langkah 8. Langkah 22, 26, 30, 34, 38, 44, 48, dan 52 membuka kembali popup karena popup menutup setelah `[Save]` dan `[✕]`.
- Langkah 23 dan 24, 31 dan 32, serta 39 dan 40 (centang kembali lalu Save) memulihkan kolom yang di-hide pada TC-GS-DIV-173; perubahan TC-GS-DIV-177 dan TC-GS-DIV-178 tidak tersimpan, sehingga tabel tetap pada konfigurasi default.
- Spec melewati sekitar 35 langkah karena TC-GS-DIV-173 menguji tiga kolom dengan blok identik (hide, Save, cek, buka kembali, centang, Save, cek) ditambah dua TC screening dan dua TC penutupan popup; semuanya satu kelas harness (fungsional) pada popup Setup Column yang sama. Blok TC-GS-DIV-173 meneruskan popup yang masih terbuka dari blok TC-GS-DIV-172, dan blok TC-GS-DIV-177 dan TC-GS-DIV-178 bergantung pada pemulihan kolom di blok TC-GS-DIV-173 (ketiga kolom tercentang kembali). Langkah pembuka popup yang berulang (22, 26, 30, 34, 38, 44, 48, 52) merupakan prefix berulang.
- Pembagian TC lintas spec: TC-GS-DIV-174, 175, 176 (reorder, pin, Reset to Default) dan TC-GS-DIV-146, 147 (Search terhadap kolom hidden) ada di spec 048; TC-GS-DIV-179 dan 234 (isolasi konfigurasi kolom dengan Modal Changelog) ada di spec 049; TC-GS-DIV-183 dan 184 (Download terhadap kolom visible) ada di spec 050.
- Temuan untuk QA:
  - TC-GS-DIV-173 Expected d: konfigurasi terakhir yang disimpan adalah ketiga kolom tampil (sama dengan default), sehingga F5 tidak membedakan konfigurasi tersimpan dari default.
  - TC-GS-DIV-172: Expected b.iii ("Preview tabel merefleksikan susunan kolom") tidak menyebut isi preview; spec hanya mengasersi preview tampil merefleksikan ketiga kolom.
  - Mekanisme menghapus preferensi kolom di browser tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
