---
id: TC-AC-LCS-E2E-110-setup-column-modal-changelog
title: "Setup Column Modal Changelog: Popup, Preview, Save, Tutup, Reset to Default, dan Cache per Tab"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-410
  - TC-AC-LCS-411
  - TC-AC-LCS-412
  - TC-AC-LCS-413
  - TC-AC-LCS-414
coverage:
  web: automated
---

# Setup Column Modal Changelog: Popup, Preview, Save, Tutup, Reset to Default, dan Cache per Tab

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Konfigurasi ketujuh tab pada nilai default (Pre-setup 7) dipulihkan lewat Fixture BE di hook `beforeEach` dan `after` suite (kemampuan disediakan tim FE/BE).
- Hook `before` men-seed Dataset L (27 entri Changelog tab Client Lifecycle, Pre-setup 8: entri ke-n pada n May 26 pukul 10:00, Action Edit, Old Value 5n, New Value 5n+3, Modified By berputar John Doe, Sarah Thompson, Budi Santoso) lewat Fixture BE (kemampuan disediakan tim FE/BE; menimpa riwayat tab itu); hook `after` mengembalikan dataset ke keadaan awal.
- Hook `before` men-seed dataset Changelog kecil tab Recycle Bin (3 entri, Pre-setup 9) lewat Fixture BE; hook `after` mengembalikan dataset ke keadaan awal.
- General Settings: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC (tidak diubah spec ini).
- Preferensi kolom modal Changelog (Column Visibility dan Setup Column) yang tersimpan di browser dihapus di hook `after` (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Data uji mengacu ke fixture `Fixture.plansLicensingLifecycleSettings` (nilai default tiap tab dan dataset Changelog); fixture belum ada dan disediakan tim FE/BE.
- Konfigurasi Lifecycle Settings bersifat platform-wide dan Changelog bersifat permanen; suite berjalan serial (`parallel: false`).
- Env var: `AC_TC_PASSWORD` (password Total Control Admin Console, satu nama satu arti).

## Test Steps

### TC-AC-LCS-410: Screening popup Setup Column dari modal Changelog

1. Klik icon Changelog di pojok kanan atas panel tab Client Lifecycle
2. Klik header `(⋯)`
3. Klik "Setup Column..."
4. Susuri popup dari atas ke bawah
5. Verifikasi Header: Title "Setup Column"
6. Verifikasi Header: Deskripsi "Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns."
7. Verifikasi Header: tombol close `[✕]`
8. Verifikasi Body: daftar `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By`
9. Verifikasi Body: checkbox seluruh item tercentang (Hideable) dan enabled
10. Verifikasi Body: seluruh item memiliki drag handle
11. Verifikasi Body: seluruh item memiliki icon Pin
12. Verifikasi Body: tidak ada kolom Curated tambahan
13. Verifikasi Body: Live Preview tabel di belakang popup merefleksikan urutan dan visibilitas kolom
14. Verifikasi Footer: `[Reset to Default]` (Text, primary) dan `[Save]` (filled, success)
15. Verifikasi Footer: tidak ada tombol `[Cancel]`

### TC-AC-LCS-412: Menutup popup Setup Column dengan [✕] membuang perubahan preview

16. Uncheck `New Value` pada popup Setup Column yang masih terbuka
17. Klik `[✕]` pada popup
18. Verifikasi popup tertutup tanpa Save
19. Verifikasi kolom `New Value` kembali tampil pada tabel

### TC-AC-LCS-411: Perubahan di popup Setup Column hanya preview sampai Save lalu tersimpan di cache

20. Klik header `(⋯)`
21. Klik "Setup Column..."
22. Uncheck `New Value`
23. Verifikasi kolom `New Value` hilang pada preview tabel di balik popup
24. Klik `[Save]`
25. Verifikasi popup tertutup
26. Verifikasi kolom `New Value` tetap tersembunyi
27. Tutup modal dengan `[✕]`
28. Klik icon Changelog di pojok kanan atas panel tab Client Lifecycle
29. Verifikasi kolom `New Value` tetap tersembunyi (cache browser)

### TC-AC-LCS-413: Reset to Default pada popup Setup Column mengembalikan konfigurasi default sebagai preview

30. Klik header `(⋯)`
31. Klik "Setup Column..."
32. Klik `[Reset to Default]`
33. Verifikasi kolom `New Value` tercentang kembali pada preview
34. Verifikasi urutan kolom default pada preview: `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By`
35. Klik `[Save]`
36. Verifikasi tabel menampilkan keenam kolom default

### TC-AC-LCS-414: Cache Setup Column modal Changelog independen antar tab

37. Klik header `(⋯)`
38. Uncheck `Old Value`
39. Tutup modal dengan `[✕]`
40. Klik tab Recycle Bin
41. Klik icon Changelog di pojok kanan atas panel tab Recycle Bin
42. Verifikasi modal Changelog Recycle Bin menampilkan keenam kolom termasuk `Old Value`

## Notes

- Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC dalam spec: TC-AC-LCS-410, TC-AC-LCS-412, TC-AC-LCS-411, TC-AC-LCS-413, TC-AC-LCS-414. TC-AC-LCS-412 dijalankan sebelum TC-AC-LCS-411 supaya kolom masih default dan popup masih terbuka dari TC-AC-LCS-410; kolom `New Value` yang disembunyikan dan disimpan TC-AC-LCS-411 menjadi precondition TC-AC-LCS-413 (dipakai sebagai precondition TC, tidak diasersi); `[Save]` TC-AC-LCS-413 mengembalikan konfigurasi default sebelum TC-AC-LCS-414.
- Langkah penghubung: menutup modal dan membuka modal kembali pada TC-AC-LCS-411 adalah langkah TC; menutup modal sebelum pindah tab pada TC-AC-LCS-414; popup Setup Column pada langkah pertama TC-AC-LCS-412 masih terbuka dari TC-AC-LCS-410.
- Hook `after` suite menghapus preferensi kolom modal Changelog yang tersimpan spec ini (kolom `Old Value` Client Lifecycle pada TC-AC-LCS-414 tidak disimpan lewat Save tetapi tetap dihapus sebagai cadangan).
- Spec ini melewati sekitar 35 langkah (di atas smell): lima blok TC memakai popup Setup Column modal Changelog yang sama. Alasan mempertahankan satu spec: seluruh blok satu kelas harness dengan dataset yang sama dan menyambung state konfigurasi kolom (hasil Save TC-AC-LCS-411 menjadi precondition TC-AC-LCS-413 dan dikembalikan ke default oleh `[Save]` TC-AC-LCS-413), sehingga memecahnya menambah seeding dan pemulihan preferensi kolom tanpa memberi isolasi lebih.
- Temuan untuk QA:
  - Post Condition TC-AC-LCS-411 ("Konfigurasi kolom tersimpan di cache browser") tidak punya langkah observasi sendiri; Expected langkah 4 TC (kolom tetap tersembunyi setelah modal dibuka kembali) menjadi observasinya.
  - Precondition TC-AC-LCS-414 menyebut Dataset L tersedia pada modal Client Lifecycle dan dataset tab Recycle Bin tersedia; TC tidak menyebut jumlah entri sehingga spec memakai Dataset L (27 entri) dan dataset kecil Recycle Bin (3 entri).
  - Post Condition seluruh TC ("Tidak ada perubahan data") tidak punya langkah observasi dan tidak diasersi.
