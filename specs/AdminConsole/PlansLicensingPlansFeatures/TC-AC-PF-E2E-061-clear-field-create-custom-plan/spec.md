---
id: TC-AC-PF-E2E-061-clear-field-create-custom-plan
title: "Clear Field Create Custom Plan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-153
  - TC-AC-PF-154
  - TC-AC-PF-618
coverage:
  web: automated
---

# Clear Field Create Custom Plan

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Principal), akun #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.AC_TC_PASSWORD`); halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_ac-plans-features` true dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): sesi API aktor dan fixture backend idempoten untuk memulihkan Dataset Pre-setup dan menghapus plan buatan spec. General Settings (Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC) disiapkan fixture sebagai precondition TC dan tidak diubah spec.
- Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12): nilai Pre-setup dirujuk lewat kunci fixture yang dibuat tim FE; password dan token tidak ditulis di spec.
- Data Pre-setup: Dataset Plan A dengan default plan `Growth` (Group count 3).
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup (`Growth`) dipakai apa adanya, hanya dibaca (Template); pemulihan Dataset dijamin fixture backend idempoten yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini.
- Data Dinamis: Plan Name `Paket Dibersihkan-{runId}-061` (bersuffix `-{runId}-061`); tidak ada plan yang tersimpan.
- State global: Dataset Pre-setup bersama; suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Spec berakhir pada form tanpa nilai (pasca `[Submit]` ditolak); hook `after` memulihkan Dataset.

## Test Steps

### Clear Field menghapus error dan memulihkan fokus (TC-AC-PF-618)

1. Buka tab `Custom`, sub-tab `Active`
2. Klik `+ Custom Plan` pada toolbar
3. Klik `[Submit]` tanpa mengisi apa pun
4. Verifikasi pesan inline `Product must not be empty`, `Template must not be empty`, dan `Plan name must not be empty` muncul
5. Verifikasi border merah pada ketiga field tersebut
6. Klik `[Clear Field]`
7. Verifikasi seluruh pesan error inline dan border merah hilang (form kembali pristine)
8. Verifikasi fokus berada pada field pertama (Product)
9. Verifikasi form tetap terbuka tanpa dialog

### Clear Field mengembalikan form ke kondisi awal (TC-AC-PF-153)

10. Pilih Product `FAMS` dan Template `Growth`, isi Plan Name `Paket Dibersihkan-{runId}-061`
11. Ubah Group count menjadi `25`
12. Klik `[Clear Field]`
13. Verifikasi Product kembali kosong dengan placeholder `Select product`
14. Verifikasi Plan Name kembali kosong dengan placeholder `Enter plan name`
15. Verifikasi Template kembali ke `Select template`
16. Verifikasi Capacity Toggles, Binary Toggles, dan Feature Suites kembali kosong sampai Template dipilih lagi
17. Verifikasi tidak ada dialog konfirmasi dan tidak ada dialog Unsaved Changes, dan form tetap terbuka

### Submit sesudah Clear Field (TC-AC-PF-154)

18. Isi Product `FAMS`, Template `Growth`, dan Plan Name `Paket Dibersihkan-{runId}-061`
19. Klik `[Clear Field]`
20. Klik `[Submit]`
21. Verifikasi pesan inline `Product must not be empty`, `Template must not be empty`, dan `Plan name must not be empty` muncul
22. Verifikasi form tetap terbuka dan tidak berpindah ke Plan Detail (tidak ada plan baru)

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1.
- Urutan TC di spec: TC-AC-PF-618 pertama karena TC itu membangun keadaan error dari form kosong; TC-AC-PF-153 menyusul dengan form berisi; TC-AC-PF-154 terakhir karena Submit-nya ditolak.
- "Tidak ada plan baru" diamati lewat form yang tetap terbuka tanpa berpindah ke Plan Detail. Spec berakhir pada form pristine (pesan error validasi tidak membuat form dirty) sehingga tidak ada langkah pemulihan tambahan.
- Temuan untuk QA: TC-AC-PF-618 menyebut Expected "fokus berada pada field pertama (Product)" tanpa mengatakan kapan fokus diasersi; spec mengasersinya segera sesudah `[Clear Field]` (8b butir 5).
