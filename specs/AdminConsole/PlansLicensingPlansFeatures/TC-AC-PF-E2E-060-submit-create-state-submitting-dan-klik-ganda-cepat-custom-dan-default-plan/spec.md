---
id: TC-AC-PF-E2E-060-submit-create-state-submitting-dan-klik-ganda-cepat-custom-dan-default-plan
title: "Submit Create: State Submitting dan Klik Ganda Cepat pada Custom dan Default Plan"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PF-162
  - TC-AC-PF-163
  - TC-AC-PF-194
  - TC-AC-PF-700
coverage:
  web: automated
---

# Submit Create: State Submitting dan Klik Ganda Cepat pada Custom dan Default Plan

## Prerequisites

- Mode: FE+BE (intercept parsial atas backend nyata: `Spectra.intercept` menunda respons Create pada TC-AC-PF-162 dan TC-AC-PF-700).
- Login di hook `before` spec ini sebagai Total Control (Principal), akun #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.AC_TC_PASSWORD`); halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_ac-plans-features` true dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): sesi API aktor dan fixture backend idempoten untuk memulihkan Dataset Pre-setup dan menghapus plan buatan spec. General Settings (Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC) disiapkan fixture sebagai precondition TC dan tidak diubah spec.
- Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12): nilai Pre-setup dirujuk lewat kunci fixture yang dibuat tim FE; password dan token tidak ditulis di spec.
- Data Pre-setup: Dataset Plan A dengan default plan `Growth` sebagai Template (TC-AC-PF-162, TC-AC-PF-163, TC-AC-PF-700) dan Dataset Plan V2 (FAMS dengan slot Paid tersisa) untuk TC-AC-PF-194; slot Free SAMS tersedia untuk TC-AC-PF-700. Kedua Dataset disediakan fixture backend dan dipulihkan.
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup (`Growth`) dipakai apa adanya, hanya dibaca (Template); pemulihan Dataset dijamin fixture backend idempoten yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini.
- Data Dinamis: nama bersuffix `-{runId}-060`: custom plan `Paket In Flight-{runId}-060` dan `Paket Klik Ganda-{runId}-060`; default plan `Paket In Flight-{runId}-060` dan `Paket Klik Ganda Default-{runId}-060`. Keempat plan tersimpan karena respons yang ditunda dilepas.
- State global: Dataset Pre-setup bersama; suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Pembersihan: hook `after` menghapus plan buatan spec ini (nama bersuffix `-{runId}-060`) lewat fixture backend, memulihkan Dataset, dan mengembalikan sesi ke akun default suite.

## Test Steps

### Submit berlangsung pada Custom Plan (TC-AC-PF-162)

1. Buka tab `Custom`, sub-tab `Active`
2. Klik `+ Custom Plan` pada toolbar
3. Aktifkan `Spectra.intercept` yang menunda respons Create custom plan
4. Isi Product `FAMS`, Template `Growth`, dan Plan Name `Paket In Flight-{runId}-060`
5. Klik `[Submit]` dan amati form sebelum respons diterima
6. Verifikasi tombol `[Submit]` menampilkan indikator loading dan berstatus Disabled
7. Verifikasi field input dan tombol `[Clear Field]` tidak dapat dipakai selama request berlangsung
8. Lepas tahanan respons dan hapus intercept, lalu tunggu aksi selesai

### Klik ganda pada Custom Plan (TC-AC-PF-163)

9. Klik breadcrumb sub-tab `Active`
10. Klik `+ Custom Plan` pada toolbar
11. Isi Product `FAMS`, Template `Growth`, dan Plan Name `Paket Klik Ganda-{runId}-060`
12. Tunggu toast lama hilang otomatis
13. Klik `[Submit]` dua kali dengan cepat
14. Verifikasi satu toast sukses: "Success, custom plan has been created."
15. Klik breadcrumb sub-tab `Active`, lalu ketik Search `Paket Klik Ganda-{runId}-060`, tekan Enter
16. Verifikasi hanya satu request diproses dan satu plan `Paket Klik Ganda-{runId}-060` tersimpan (tepat satu baris)

### Submit berlangsung pada Default Plan (TC-AC-PF-700)

17. Buka tab `Default`, sub-tab `Active`
18. Klik `+ Default Plan`
19. Aktifkan `Spectra.intercept` yang menunda respons Create default plan
20. Pilih Product `SAMS`, Pricing Type `Free`, dan isi Plan Name `Paket In Flight-{runId}-060`
21. Klik `[Submit]` dan amati form sebelum respons diterima
22. Verifikasi tombol `[Submit]` menampilkan indikator loading dan berstatus Disabled
23. Verifikasi field input dan tombol `[Clear Field]` tidak dapat dipakai selama request berlangsung
24. Lepas tahanan respons dan hapus intercept, lalu tunggu aksi selesai

### Klik ganda pada Default Plan (TC-AC-PF-194)

25. Klik breadcrumb sub-tab `Active`
26. Klik `+ Default Plan`
27. Pilih Product `FAMS`, Pricing Type `Paid`, dan isi Plan Name `Paket Klik Ganda Default-{runId}-060`
28. Tunggu toast lama hilang otomatis
29. Klik `[Submit]` dua kali dengan cepat
30. Verifikasi satu toast sukses: "Success, default plan has been created."
31. Klik breadcrumb sub-tab `Active`, lalu ketik Search `Paket Klik Ganda Default-{runId}-060`, tekan Enter
32. Verifikasi satu default plan `Paket Klik Ganda Default-{runId}-060` tersimpan (tepat satu baris)

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 8, 9, 12, 15, 17, 24, 25, 28, 31.
- Tahanan respons pada TC-AC-PF-162 dan TC-AC-PF-700 hanya untuk mengamati state UI (loading, Disabled) dan dilepas segera sesudah asersi (S-09); karena itu bukan kelas b.
- Langkah penghubung: Search untuk menemukan baris target (R-16), breadcrumb sub-tab `Active`, dan "Tunggu toast lama hilang otomatis" sebelum hitungan satu toast (R-12). Hasil Submit yang ditunda tidak diasersi, sehingga langkah tunggu aksi selesai dituliskan sebelum pindah surface (bagian 8b butir 8).
- Temuan untuk QA: (1) Post Condition TC-AC-PF-162 dan TC-AC-PF-700 "Tidak ada perubahan data" bertentangan dengan perilaku sesudah respons dilepas: plan tetap tersimpan (spec membersihkannya di hook `after`). (2) "Hanya satu request diproses" pada TC-AC-PF-163 dan TC-AC-PF-194 hanya teramati lewat satu baris dan satu toast; jumlah request tidak diasersi langsung. (3) TC-AC-PF-194 dan TC-AC-PF-700 menguji Create Default Plan, tetapi berada di antara TC Create Custom Plan pada section TC yang sama.
