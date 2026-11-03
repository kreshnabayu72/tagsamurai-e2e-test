---
id: TC-GS-NLU-E2E-123-resilience-tulis-kegagalan-5xx-saat-create-dan-edit-mempertahankan
title: "Resilience tulis: kegagalan 5xx saat Create dan Edit mempertahankan isian"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-NLU-93
  - TC-GS-NLU-172
coverage:
  web: automated
---

# Resilience tulis: kegagalan 5xx saat Create dan Edit mempertahankan isian

## Prerequisites

- Mode: FE+BE. Spec memaksa respons 500 pada request simpan lewat `Spectra.intercept()` di atas backend nyata; hasil retry diasersi dari backend nyata.
- Akun: Total Control, `Siti Nurhaliza (Siti N)`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Kemampuan teknis: `Spectra.intercept()` untuk memaksa respons 500 pada request yang disebut tiap langkah, parsial di atas backend nyata (bagian 6); nama endpoint ditentukan tim FE pada tahap script (S-13). Hook `after` melepas semua intercept walau spec gagal di tengah.
- Data Pre-setup No. 9 sampai 13 (Position `Driver` dan `Manager`; Division `Operations`, `Warehouse`, `Logistics`, `Finance`; Login User `Ahmad Fauzi` dan `Dewi Anggraini`; Custom Field dasar) hanya dibaca, tidak diubah atau dihapus.
- Request yang dipaksa 500: simpan Create (TC-GS-NLU-93) dan simpan Edit (TC-GS-NLU-172), satu per satu dan dilepas sebelum retry.
- Data milik spec (di-seed hook `before` lewat API, dibersihkan hook `after`; mekanisme seeding dan penghapusan disediakan tim FE/BE): `Edit Target Tiga Satu {runId}-123` (First Name `Edit`, Last Name `Target Tiga Satu {runId}-123`, Division `Operations`, Email `edittargettigasatu+{runId}-123@qwertysystem.net`, Represented By `Ahmad Fauzi`, Active).
- Data yang dibuat TC-GS-NLU-93 lewat UI: First Name `Rudi`, Last Name `Hartono {runId}-123`, Division `Logistics`, Email `rudihartono+{runId}-123@qwertysystem.net`, Represented By `Ahmad Fauzi`.
- Pemulihan: hook `after` melepas intercept dan menghapus lewat API semua data `{runId}-123` yang tersisa.
- Suite berjalan serial (`parallel: false`).
- Fixture `fixtures/non-login-user.json` untuk nilai data Pre-setup dan Dinamis belum ada; disediakan tim FE (S-12). Nilai di langkah ditulis literal sampai fixture tersedia.

## Test Steps

### TC-GS-NLU-93: Kegagalan server 5xx saat Submit mempertahankan isian pada Popup Create

1. Klik `[+ Non-Login User]`
2. Isi First Name `Rudi`, Last Name `Hartono {runId}-123`, Division `Logistics`, Email `rudihartono+{runId}-123@qwertysystem.net`
3. Pilih Represented By `Ahmad Fauzi` lewat popup Select User
4. Pasang intercept yang memaksa respons 500 untuk request simpan Create
5. Klik `[Submit]`
6. Verifikasi Toast error `Error, failed to create non-login user.`
7. Verifikasi Popup Create tetap terbuka
8. Verifikasi isian dipertahankan: First Name `Rudi`, Last Name `Hartono {runId}-123`, Division `Logistics`, Email `rudihartono+{runId}-123@qwertysystem.net`, Represented By `Ahmad Fauzi`
9. Verifikasi tombol `[Submit]` aktif kembali
10. Lepas intercept (pulihkan response)
11. Klik `[Submit]` lagi
12. Verifikasi Toast sukses `Success, non-login user has been created.`

### TC-GS-NLU-172: Kegagalan server 5xx saat Save mempertahankan isian pada Popup Edit

13. Ketik Search `Edit Target Tiga Satu {runId}-123`, tekan Enter, klik `⋯` baris `Edit Target Tiga Satu {runId}-123` > `Edit`
14. Ubah First Name menjadi `Rudi`
15. Pasang intercept yang memaksa respons 500 untuk request simpan Edit
16. Klik `[Save]`
17. Verifikasi Toast error `Error, failed to update non-login user.`
18. Verifikasi Popup Edit tetap terbuka
19. Verifikasi isian dipertahankan: First Name `Rudi`
20. Verifikasi tombol `[Save]` aktif kembali
21. Lepas intercept (pulihkan response)
22. Klik `[Save]` lagi
23. Verifikasi Toast sukses `Success, non-login user has been updated.`

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Kelas b (fault injection) ringan: intercept parsial di atas backend nyata; intercept dilepas pada langkah 10 dan 21 sebelum retry (S-09).
- Langkah penghubung (S-03, R-16): langkah 1 (membuka popup Create), langkah 13 (Search record yang dicari dan membuka Popup Edit), langkah 4, 15 (memasang intercept), langkah 10, 21 (melepas intercept).
- Temuan untuk QA:
  - TC-GS-NLU-93 dan 172 Expected c ("Retry setelah pemulihan: sukses") tidak menyebut tanda sukses; spec memakai Toast sukses `Success, non-login user has been created.` dan `Success, non-login user has been updated.` seperti TC create dan edit lain.
  - TC-GS-NLU-172 memakai baris Edit Target 31 (Pre-setup No. 12); spec memakai record milik spec yang setara.
