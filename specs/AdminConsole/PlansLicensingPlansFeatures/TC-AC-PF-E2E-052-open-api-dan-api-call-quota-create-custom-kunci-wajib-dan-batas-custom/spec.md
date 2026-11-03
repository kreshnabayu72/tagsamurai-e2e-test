---
id: TC-AC-PF-E2E-052-open-api-dan-api-call-quota-create-custom-kunci-wajib-dan-batas-custom
title: "Open API dan API Call Quota Create Custom Plan: Kunci, Wajib, dan Batas Custom"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PF-130
  - TC-AC-PF-131
  - TC-AC-PF-132
  - TC-AC-PF-133
coverage:
  web: automated
---

# Open API dan API Call Quota Create Custom Plan: Kunci, Wajib, dan Batas Custom

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Principal), akun #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.AC_TC_PASSWORD`); halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_ac-plans-features` true dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): sesi API aktor dan fixture backend idempoten untuk memulihkan Dataset Pre-setup dan menghapus plan buatan spec. General Settings (Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC) disiapkan fixture sebagai precondition TC dan tidak diubah spec.
- Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12): nilai Pre-setup dirujuk lewat kunci fixture yang dibuat tim FE; password dan token tidak ditulis di spec.
- Data Pre-setup: Dataset Plan A dengan default plan `Growth` (Open API ON).
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup (`Growth`) dipakai apa adanya, hanya dibaca (Template); pemulihan Dataset dijamin fixture backend idempoten yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini.
- Data Dinamis: Plan Name bersuffix `-{runId}-052`: `Paket Quota Kosong-{runId}-052`, `Paket Quota Bawah-{runId}-052`, `Paket Quota Atas-{runId}-052`. Plan yang tersimpan: `Paket Quota Bawah-{runId}-052` (API call quota 100000) dan `Paket Quota Atas-{runId}-052` (API call quota 10000000).
- State global: Dataset Pre-setup bersama; suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Pembersihan: hook `after` menghapus plan buatan spec ini (nama bersuffix `-{runId}-052`) lewat fixture backend, memulihkan Dataset, dan mengembalikan sesi ke akun default suite.

## Test Steps

### Open API dan API call quota (TC-AC-PF-130)

1. Buka tab `Custom`, sub-tab `Active`
2. Klik `+ Custom Plan` pada toolbar
3. Pilih Product `FAMS` dan Template `Growth`
4. Matikan toggle Open API
5. Verifikasi nilai API call quota otomatis reset ke `—` dan field terkunci (Disabled, tetap tampil)
6. Hover field API call quota
7. Verifikasi tooltip `Turn on Open API to set an API call quota.` tampil
8. Nyalakan toggle Open API
9. Verifikasi field API call quota aktif kembali
10. Verifikasi tooltip `Turn on Open API to set an API call quota.` hilang

### API call quota kosong (TC-AC-PF-131)

11. Isi Plan Name `Paket Quota Kosong-{runId}-052`
12. Matikan Open API lalu nyalakan lagi sehingga API call quota `—`
13. Klik `[Submit]`
14. Verifikasi pesan inline `API call quota must not be empty` muncul di bawah field API call quota setelah Submit
15. Verifikasi form tetap terbuka dengan input dipertahankan
16. Verifikasi tidak ada toast sukses dan tidak ada plan baru (halaman tidak berpindah ke Plan Detail)

### Batas bawah (TC-AC-PF-132)

17. Ganti isi Plan Name dengan `Paket Quota Bawah-{runId}-052`
18. Pilih API call quota `Custom` lalu isi `99999` dan klik `[Submit]`
19. Verifikasi nilai `99999` ditolak setelah Submit dengan pesan `Value must be between 100,000 and 10,000,000 calls/month`
20. Ubah nilai menjadi `100000` dan klik `[Submit]`
21. Verifikasi toast sukses: "Success, custom plan has been created."
22. Verifikasi Tab Overview baris API call quota menampilkan `100K/month` (nilai sama dengan preset tampil sebagai preset)

### Batas atas (TC-AC-PF-133)

23. Klik breadcrumb sub-tab `Active`
24. Klik `+ Custom Plan` pada toolbar
25. Pilih Product `FAMS`, Template `Growth`, isi Plan Name `Paket Quota Atas-{runId}-052`
26. Pilih API call quota `Custom` lalu isi `10000001` dan klik `[Submit]`
27. Verifikasi nilai `10000001` ditolak dengan pesan `Value must be between 100,000 and 10,000,000 calls/month`
28. Ubah nilai menjadi `10000000` dan klik `[Submit]`
29. Verifikasi toast sukses: "Success, custom plan has been created."

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 23.
- Urutan TC di spec: TC-AC-PF-130 dan TC-AC-PF-131 (penolakan, tanpa plan tersimpan) sebelum TC-AC-PF-132 dan TC-AC-PF-133 (tersimpan), mengikuti S-10. Plan Name pada TC-AC-PF-132 diganti pada form yang sama sesudah TC-AC-PF-131 agar nama plan tersimpan sesuai TC.
- Langkah penghubung: breadcrumb sub-tab `Active` untuk membuka form baru setelah plan tersimpan; spec berakhir pada Plan Detail tanpa form dirty.
- Temuan untuk QA: (1) Asersi "Tab Overview baris API call quota" TC-AC-PF-132 tidak punya langkah "Buka Tab Overview" di TC (TC-AC-PF-135 punya); spec mengasersi tanpa langkah tambahan. (2) Expected b TC-AC-PF-133 hanya menyebut toast sukses tanpa nilai tersimpan pada Tab Overview, padahal Post Condition menyebut kuota kustom 10.000.000; tidak diasersi karena TC tidak memberi langkah observasi.
