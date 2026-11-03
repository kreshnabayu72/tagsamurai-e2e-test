---
id: TC-AC-PF-E2E-054-dependency-d-2-dan-d-4-pada-create-custom-plan
title: "Dependency D-2 dan D-4 pada Create Custom Plan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-136
  - TC-AC-PF-137
  - TC-AC-PF-138
  - TC-AC-PF-139
  - TC-AC-PF-140
coverage:
  web: automated
---

# Dependency D-2 dan D-4 pada Create Custom Plan

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Principal), akun #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.AC_TC_PASSWORD`); halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_ac-plans-features` true dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): sesi API aktor dan fixture backend idempoten untuk memulihkan Dataset Pre-setup dan menghapus plan buatan spec. General Settings (Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC) disiapkan fixture sebagai precondition TC dan tidak diubah spec.
- Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12): nilai Pre-setup dirujuk lewat kunci fixture yang dibuat tim FE; password dan token tidak ditulis di spec.
- Data Pre-setup: Dataset Plan A dengan default plan `Growth` (Group count 3, Group hierarchy depth 2, License allocation per group ON).
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup (`Growth`) dipakai apa adanya, hanya dibaca (Template); pemulihan Dataset dijamin fixture backend idempoten yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini.
- Data Dinamis: tidak ada (spec tidak menyimpan plan).
- State global: Dataset Pre-setup bersama; suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Spec berakhir dengan `[Clear Field]` sehingga form tidak dirty; hook `after` memulihkan Dataset.

## Test Steps

### D-2: Group count 1 (TC-AC-PF-136)

1. Buka tab `Custom`, sub-tab `Active`
2. Klik `+ Custom Plan` pada toolbar
3. Pilih Product `FAMS` dan Template `Growth`
4. Ubah Group count menjadi `1`
5. Verifikasi Group hierarchy depth otomatis berubah dari `2` ke `1` secara real-time
6. Verifikasi inline warning "Group hierarchy depth was changed automatically because group count requires it." tampil

### D-4: Group count 1 (TC-AC-PF-137)

7. Klik `[Clear Field]` agar form kembali ke kondisi awal
8. Pilih Product `FAMS` dan Template `Growth`
9. Ubah Group count menjadi `1`
10. Verifikasi toggle License allocation per group otomatis berubah ke OFF secara real-time
11. Verifikasi inline warning "License allocation per group was changed automatically because group count requires it." tampil

### Dua penyesuaian sekaligus (TC-AC-PF-138)

12. Klik `[Clear Field]` agar form kembali ke kondisi awal
13. Pilih Product `FAMS` dan Template `Growth`
14. Ubah Group hierarchy depth menjadi `5`
15. Ubah Group count menjadi `1`
16. Verifikasi Group hierarchy depth otomatis `1`
17. Verifikasi License allocation per group otomatis OFF
18. Verifikasi inline warning "Group hierarchy depth was changed automatically because group count requires it." tampil
19. Verifikasi inline warning "License allocation per group was changed automatically because group count requires it." tampil

### Arah maju D-2 (TC-AC-PF-139)

20. Klik `[Clear Field]` agar form kembali ke kondisi awal
21. Pilih Product `FAMS` dan Template `Growth`
22. Ubah Group count menjadi `1`
23. Ubah Group hierarchy depth menjadi `2`
24. Verifikasi Group count otomatis berubah ke `3` secara real-time
25. Verifikasi Group hierarchy depth tetap `2`
26. Verifikasi inline warning "Group count was changed automatically because group hierarchy depth requires it." tampil

### Arah maju D-4 (TC-AC-PF-140)

27. Klik `[Clear Field]` agar form kembali ke kondisi awal
28. Pilih Product `FAMS` dan Template `Growth`
29. Ubah Group count menjadi `1`
30. Nyalakan toggle License allocation per group
31. Verifikasi Group count otomatis berubah ke `3` secara real-time
32. Verifikasi License allocation per group tetap ON
33. Verifikasi inline warning "Group count was changed automatically because license allocation per group requires it." tampil
34. Klik `[Clear Field]` untuk mengembalikan form ke kondisi awal tanpa dirty

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 7, 12, 20, 27, 34.
- Langkah `[Clear Field]` di antara TC mengembalikan Template dan nilai prefill ke kondisi awal (TC-AC-PF-153) sehingga setiap TC mulai dari Template `Growth` yang baru dipilih (S-09); spec berakhir tanpa form dirty.
- Temuan untuk QA: langkah TC-AC-PF-140 menyebut "(License allocation per group otomatis OFF)" sebagai kondisi antara tanpa Expected; spec tidak mengasersinya karena tidak ada Expected TC.
