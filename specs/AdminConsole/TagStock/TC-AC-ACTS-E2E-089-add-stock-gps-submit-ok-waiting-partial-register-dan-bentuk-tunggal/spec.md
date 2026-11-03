---
id: TC-AC-ACTS-E2E-089-add-stock-gps-submit-ok-waiting-partial-register-dan-bentuk-tunggal
title: "Add Stock GPS: Submit Tanpa Baris Valid (V-07), Semua OK, serta Campuran OK dan Waiting dengan Dialog Partial Register dan Cancel"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-259
  - TC-AC-ACTS-260
  - TC-AC-ACTS-261
  - TC-AC-ACTS-262
coverage:
  web: automated
---

# Add Stock GPS: Submit Tanpa Baris Valid (V-07), Semua OK, serta Campuran OK dan Waiting dengan Dialog Partial Register dan Cancel

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun ganti di tengah spec: Distributor Toggle ON (Local Registration aktif; jalur approval normal tanpa bypass E2a) `distributorOn_automated_{namaCompany}@qwertysystem.net` (Pre-setup #9), password dari `Spectra.env.AC_DIST_ON_PASSWORD`. Pergantian akun ditulis sebagai langkah eksplisit.
- Halaman awal: halaman Add Stock SKU `GPS-TRACK-CORE-G3` (Import/Manual IMEI), dibuka dari Stock List lewat row action Add Stock pada SKU itu oleh hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- SKU `GPS-TRACK-CORE-G3` (Data Pre-setup #15). Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script; nilai identifier ditulis literal seperti di TC dan dipetakan ke kunci fixture di tahap script.
- IMEI Data Dinamis #2 (`356938035643809` sampai `356938035643817`) bersifat tetap dan tidak dapat bersuffix `{runId}`; seeding idempotent dan pemulihan lewat fixture BE sebelum spec ini. IMEI `356938035643810` terdaftar sebagai unit existing berstatus Available (dipakai sebagai precondition TC, tidak diasersi). Unit `356938035643809`, `356938035643811`, dan `356938035643812` yang didaftarkan langkah 10 dihapus lewat fixture BE di hook `after`.
- Kemampuan teknis disediakan tim FE/BE: kemampuan baca jumlah unit Available SKU, jumlah Subject Tab Active, dan jumlah baris Event Log SKU (baseline, S-12).
- Env var password akun aktor: `Spectra.env.AC_TC_PASSWORD`, `Spectra.env.AC_DIST_ON_PASSWORD`. Password tidak ditulis di spec atau fixture. Nama `AC_DIST_ON_PASSWORD` adalah nama baru yang didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-259: Submit tanpa baris OK maupun Waiting menampilkan V-07

1. Tambahkan `12345` dan input kosong lewat Manual Entry (Preview hanya berisi baris Invalid Format)
2. Klik `[Submit]`
3. Verifikasi pesan "No TAGs to register. Add at least one IMEI."
4. Verifikasi `[Submit]` tidak disabled
5. Verifikasi error tampil inline di atas tombol `[Submit]`
6. Verifikasi tidak ada data tersimpan (halaman tetap di Add Stock, tanpa toast "Success, TAG has been registered.")
7. Hapus seluruh baris Preview lewat ikon hapus pada tiap baris

### TC-AC-ACTS-260: Submit GPS semua baris OK mendaftarkan unit dengan TAG Code baru

8. Catat baseline jumlah unit Available SKU dan jumlah baris Event Log SKU
9. Tambahkan tiga IMEI baru `356938035643809`, `356938035643811`, dan `356938035643812` lewat Manual Entry
10. Klik `[Submit]`
11. Verifikasi toast "Success, TAG has been registered."
12. Verifikasi halaman menavigasi ke Detail SKU > Tab Available SKU itu
13. Verifikasi tiga unit Available baru dengan TAG Code baru (selisih +3 terhadap baseline)
14. Buka modal Event Log SKU itu (Tab Add Stock)
15. Verifikasi jumlah baris Event Log SKU bertambah satu dari baseline langkah 8
16. Verifikasi baris teratas Event Log (urutan default `Date` terbaru) adalah baris Activity `Add Stock` baru dengan Success `3` dan Hardware `—`
17. Tutup modal Event Log
18. Ganti akun: klik Logout
19. Login sebagai Distributor Toggle ON (`distributorOn_automated_{namaCompany}@qwertysystem.net`)
20. Buka halaman Add Stock SKU `GPS-TRACK-CORE-G3` dari Stock List lewat row action Add Stock

### TC-AC-ACTS-261: Submit GPS campuran OK dan Waiting memunculkan Partial Register

21. Catat baseline jumlah unit Available SKU, jumlah Subject Tab Active, dan jumlah baris Event Log SKU
22. Tambahkan IMEI baru `356938035643813` dan `356938035643814` serta IMEI existing `356938035643810` lewat Manual Entry
23. Klik `[Submit]`
24. Verifikasi dialog `Partial Register`: "1 IMEI matched an existing record and will be sent for approval. Register the remaining 2 IMEIs?" dengan `[Cancel]` dan `[Continue]`

### TC-AC-ACTS-262: Partial Register GPS, [Cancel] tidak menyimpan apa pun

25. Klik `[Cancel]` pada dialog Partial Register yang tampil dari TC-AC-ACTS-261
26. Klik `[Submit]`
27. Klik `[Cancel]` pada dialog Partial Register
28. Verifikasi kembali ke Preview utuh (dua baris OK dan satu baris Waiting for Approval)
29. Verifikasi tidak ada unit baru, Subject baru, atau entri Event Log baru (selisih nol terhadap baseline)
30. Hapus seluruh baris Preview lewat ikon hapus pada tiap baris

## Notes

- Mode: FE+BE.
- Urutan TC: TC-AC-ACTS-259 dan TC-AC-ACTS-260 (Total Control) lebih dulu, lalu satu kali ganti akun ke Distributor Toggle ON di langkah 18 untuk TC-AC-ACTS-261 dan TC-AC-ACTS-262 (S-07, S-10). Karena TC-AC-ACTS-260 memakai bypass E2a Total Control, TC-AC-ACTS-261 dan TC-AC-ACTS-262 memakai Distributor supaya baris Waiting terbentuk.
- Cara baca entri audit trail baru (S-12, S-14): jumlah dicatat sebelum aksi pemicu, selisihnya diverifikasi, lalu baris teratas urutan default `Date` terbaru dibaca; bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya. Pada TC-AC-ACTS-260 baris Event Log baru dibaca setelah selisih satu dari baseline langkah 8.
- Langkah penghubung tanpa Verifikasi (S-03): "Hapus seluruh baris Preview lewat ikon hapus pada tiap baris" (S-09), langkah mencatat baseline (S-12), langkah ganti akun dan buka halaman Add Stock, serta langkah menutup dialog Partial Register dari TC-AC-ACTS-261 sebelum TC-AC-ACTS-262 menjalankan langkahnya sendiri. Langkah "Tutup modal Event Log" menutup modal sebelum pindah surface atau ganti akun (pemulihan state, S-09).
- Asersi selisih nol pada TC-AC-ACTS-262 ("tidak ada unit, Subject, atau log tersimpan") memakai baseline dan bukan absence log kelas g: ini asersi jumlah (prinsip 13g, bagian akhir).
- Temuan untuk QA:
  - TC-AC-ACTS-259 mensyaratkan Preview "hanya berisi baris Invalid Format dan Duplicate", tetapi baris Duplicate in File/List selalu menyertai kemunculan pertama berstatus OK atau Waiting (TC-AC-ACTS-248, TC-AC-ACTS-763), sehingga keadaan itu tidak dapat dibentuk; spec memakai Preview yang hanya berisi baris Invalid Format.
  - TC-AC-ACTS-260 menyebut "buka Activity Log" tanpa Expected; Activity Log tidak diasersi.
  - TC-AC-ACTS-261 dan TC-AC-ACTS-262 menyebut "Preview campuran" tanpa nilai; spec memakai dua IMEI baru dan satu IMEI existing.
- Langkah penghubung tambahan (S-03): "Tutup modal Event Log" (langkah 17) sebelum ganti akun, supaya modal tidak tertinggal saat sesi berpindah.
