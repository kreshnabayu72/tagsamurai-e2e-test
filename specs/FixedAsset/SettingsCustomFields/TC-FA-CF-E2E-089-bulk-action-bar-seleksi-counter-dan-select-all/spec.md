---
id: TC-FA-CF-E2E-089-bulk-action-bar-seleksi-counter-dan-select-all
title: "Bulk Action Bar: Varian Tombol, Counter, Clear Seleksi, Select All, dan Retensi Seleksi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-325
  - TC-FA-CF-326
  - TC-FA-CF-327
  - TC-FA-CF-328
  - TC-FA-CF-329
  - TC-FA-CF-347
  - TC-FA-CF-348
coverage:
  web: automated
---

# Bulk Action Bar: Varian Tombol, Counter, Clear Seleksi, Select All, dan Retensi Seleksi

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): blok terakhir (TC-FA-CF-348) menonaktifkan field baseline Company Alpha.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson, Modified By `Sarah J`) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Data baseline Company Alpha (Pre-setup #11 dan #12), tab General delapan baris dalam satu halaman (ukuran halaman default 10): `Asset Serial Tag` (Active), `Legacy Tag` (Active), `Depreciated Ratio` (Inactive), `Storage Capacity`, `Equipment Class`, `Operating Voltage`, `Total Cost`, `Compliance File`. Hook `before` memulihkan baseline lewat seed reset Company (disediakan tim FE/BE; fixture baru `Fixture.faCustomFields.baseline`); spec ini menonaktifkan `Asset Serial Tag` pada langkah 35 dan hook `after` memulihkan.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: mencentang baris tabel, Search tabel Custom Fields.
- State global: tidak ada yang diubah selain status `Asset Serial Tag` dan flag Guided Tooltip (dipulihkan hook `after`).

## Test Steps

### TC-FA-CF-325: Seleksi hanya baris Inactive

1. Centang baris `Depreciated Ratio`
2. Verifikasi Bulk Action Bar tampil dengan counter `1 custom field selected`
3. Verifikasi tombol `[Activate]` dan `[Delete]` tampil
4. Verifikasi tombol `[Deactivate]` Hidden
5. Hapus centang baris `Depreciated Ratio`

### TC-FA-CF-326: Seleksi hanya baris Active

6. Centang baris `Asset Serial Tag` dan `Legacy Tag`
7. Verifikasi Bulk Action Bar menampilkan counter `2 custom fields selected`
8. Verifikasi tombol `[Deactivate]` dan `[Delete]` tampil
9. Verifikasi tombol `[Activate]` Hidden
10. Hapus centang baris `Legacy Tag`

### TC-FA-CF-327: Seleksi campuran Active dan Inactive

11. Centang baris `Depreciated Ratio`
12. Verifikasi tombol `[Activate]`, `[Deactivate]`, dan `[Delete]` tampil bersamaan

### TC-FA-CF-328: Icon clear pada Bulk Action Bar

13. Klik icon `[✕]` pada Bulk Action Bar
14. Verifikasi seluruh centang dibatalkan
15. Verifikasi Bulk Action Bar hilang

### TC-FA-CF-329: Counter satu dan jamak serta mengikuti uncheck

16. Centang baris `Asset Serial Tag`
17. Verifikasi counter Bulk Action Bar `1 custom field selected`
18. Centang baris `Legacy Tag`
19. Verifikasi counter Bulk Action Bar `2 custom fields selected`
20. Hapus centang baris `Asset Serial Tag`
21. Verifikasi counter Bulk Action Bar `1 custom field selected`
22. Klik icon `[✕]` pada Bulk Action Bar

### TC-FA-CF-347: Select All berubah menjadi Unselect All

23. Centang baris `Asset Serial Tag`
24. Klik `Select All (8 records)`
25. Verifikasi seluruh delapan baris terpilih
26. Verifikasi tombol berubah menjadi `Unselect All`
27. Klik `Unselect All`
28. Verifikasi seluruh seleksi dibatalkan
29. Verifikasi Bulk Action Bar tertutup

### TC-FA-CF-348: Seleksi bertahan saat Search diubah dan reset setelah aksi ter-commit

30. Centang baris `Asset Serial Tag`
31. Ketik Search `Legacy`, tekan Enter
32. Klik `(←)` pada kotak Search
33. Verifikasi centang baris `Asset Serial Tag` tetap terpilih
34. Klik `[Deactivate]` pada Bulk Action Bar
35. Klik `[Deactivate]` pada dialog
36. Verifikasi Bulk Action Bar hilang
37. Verifikasi seleksi 0

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (37 langkah). Seluruhnya satu topik (Bulk Action Bar dan seleksi baris) pada satu dataset baseline Company Alpha; tujuh blok berdiri sendiri dan hanya mengamati seleksi, kecuali blok terakhir yang menonaktifkan `Asset Serial Tag` di akhir spec (S-10).
- Urutan TC dalam spec: 325, 326, 327, 328, 329, 347, 348; sama dengan urutan TC sumber, dan aksi yang menonaktifkan data (TC-FA-CF-348) paling akhir (S-10). Langkah "Centang dua baris" TC-FA-CF-328 dipenuhi seleksi dua baris `Asset Serial Tag` (sisa langkah 6) dan `Depreciated Ratio` (langkah 11) sehingga langkah 13 langsung mengklik `[✕]`.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 5, 10, dan 22 (membersihkan seleksi sebelum blok berikutnya; S-09), langkah 13 (klik `[✕]` adalah aksi TC-FA-CF-328 yang juga membersihkan seleksi), dan langkah 31 serta 32 (Search `Legacy` dan menutup input Search lewat `(←)`; langkah TC-FA-CF-348).
- Langkah 3 dan 4, 8 dan 9 memecah "tombol tampil" dan "tombol Hidden" menjadi `Verifikasi` terpisah (S-01, dua klausa).
- Temuan untuk QA:
  - TC-FA-CF-348 langkah 3 ("Bersihkan Search") tidak menyebut cara membersihkan; spec memakai `(←)` pada kotak Search (bagian 8b butir 9).
  - TC-FA-CF-348 langkah 4 ("Jalankan Bulk Deactivate pada seleksi") tidak menyebut tombol konfirmasi; spec memakai `[Deactivate]` pada Bulk Action Bar lalu `[Deactivate]` pada dialog (sesuai TC-FA-CF-331).
  - TC-FA-CF-347 mensyaratkan delapan baris tab General; benar pada baseline Pre-setup #11 dan #12.
  - TC-FA-CF-348 Expected butir b tidak menyebut toast hasil Deactivate; tidak diasersi.
