---
id: TC-AC-ACTS-E2E-114-defense-in-depth-distributor-suspended-read-only-capability-parsial-dan-payload-note
title: "Defense-in-Depth: Distributor Suspended Request Tulis Ditolak, Read Only, Capability Parsial, Pemegang Update Tidak Dapat Approve atau Reject, dan Payload XSS/SQL di Approval Note"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACTS-706
  - TC-AC-ACTS-709
  - TC-AC-ACTS-784
  - TC-AC-ACTS-785
  - TC-AC-ACTS-786
coverage:
  web: automated
---

# Defense-in-Depth: Distributor Suspended Request Tulis Ditolak, Read Only, Capability Parsial, Pemegang Update Tidak Dapat Approve atau Reject, dan Payload XSS/SQL di Approval Note

## Prerequisites

- Mode: FE+BE. Request langsung ke server lewat klien HTTP (kelas a, K-1).
- Akun aktor: Total Control Principal `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun ganti di tengah spec: Distributor dengan entitas Suspended `distributorSuspended_automated_{namaCompany}@qwertysystem.net` (Pre-setup #20), password dari `Spectra.env.AC_DIST_SUSP_PASSWORD`. Pergantian akun ditulis sebagai langkah eksplisit.
- Akun ganti di tengah spec: Read Only `readOnly_automated_{namaCompany}@qwertysystem.net` (Pre-setup #3), password dari `Spectra.env.AC_RO_PASSWORD`. Pergantian akun ditulis sebagai langkah eksplisit.
- Akun ganti di tengah spec: Manage TAG stock Read+Create `manageTagStockCreate_automated_{namaCompany}@qwertysystem.net` (Pre-setup #5), password dari `Spectra.env.AC_TS_CREATE_PASSWORD`. Pergantian akun ditulis sebagai langkah eksplisit.
- Akun ganti di tengah spec: Manage TAG stock Read+Update `manageTagStockUpdate_automated_{namaCompany}@qwertysystem.net` (Pre-setup #6), password dari `Spectra.env.AC_TS_UPDATE_PASSWORD`. Pergantian akun ditulis sebagai langkah eksplisit.
- Akun ganti di tengah spec: Manage TAG stock Read+Delete `manageTagStockDelete_automated_{namaCompany}@qwertysystem.net` (Pre-setup #7), password dari `Spectra.env.AC_TS_DELETE_PASSWORD`. Pergantian akun ditulis sebagai langkah eksplisit.
- Halaman awal spec: Approvals > TAG Stock > Tab Active untuk TC-AC-ACTS-706 (dibuka langkah 1); langkah lain adalah request langsung lewat klien HTTP.
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- Kemampuan teknis disediakan tim FE/BE: klien HTTP untuk request Add Stock, Audit Submit, Delete, Approve, Reject, dan baca; sesi API aktor per akun (login API password, token tidak dihitung sebagai sesi web); kemampuan baca status respons dan state data (jumlah unit, status unit, jumlah Subject, TAG Code) lewat fixture BE. Endpoint tidak dikarang di spec.
- Kemampuan baca jumlah baris Event Log SKU (disediakan tim FE/BE) dipakai sebagai baseline TC-AC-ACTS-706 (S-12).
- Data milik spec disiapkan seeding fixture BE (disediakan tim FE/BE): Subject Register Duplicate pending untuk TC-AC-ACTS-706 (dipakai Reject dengan payload) dan untuk TC-AC-ACTS-786, serta unit Available milik entitas aktor untuk TC-AC-ACTS-709, TC-AC-ACTS-784, dan TC-AC-ACTS-785. Status Suspended pada entitas Distributor (Pre-setup #20) tidak diubah spec ini. Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script.
- Payload Approval Note TC-AC-ACTS-706: `<script>alert(1)</script>'; DROP TABLE x;--`.
- Env var password akun aktor: `Spectra.env.AC_TC_PASSWORD`, `Spectra.env.AC_DIST_SUSP_PASSWORD`, `Spectra.env.AC_RO_PASSWORD`, `Spectra.env.AC_TS_CREATE_PASSWORD`, `Spectra.env.AC_TS_UPDATE_PASSWORD`, `Spectra.env.AC_TS_DELETE_PASSWORD`. Password tidak ditulis di spec atau fixture. Nama `AC_DIST_SUSP_PASSWORD`, `AC_TS_CREATE_PASSWORD`, `AC_TS_UPDATE_PASSWORD`, `AC_TS_DELETE_PASSWORD` adalah nama baru yang didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-706: Payload XSS dan SQL injection di Approval Note disimpan sebagai teks

1. Buka Approvals > TAG Stock > Tab Active
2. Klik `Review` pada Subject Register Duplicate pending, pilih Reject
3. Isi Approval Note `<script>alert(1)</script>'; DROP TABLE x;--`
4. Catat baseline jumlah baris Event Log SKU lewat kemampuan baca BE
5. Klik `[Submit]`
6. Tunggu aksi selesai (dialog Review tertutup)
7. Buka modal Event Log SKU
8. Verifikasi Event Log memuat baris pembanding milik SKU itu
9. Verifikasi jumlah baris Event Log bertambah 1 dari baseline
10. Verifikasi tidak ada script berjalan (tidak ada dialog `alert`)
11. Verifikasi teks payload tampil apa adanya pada baris teratas Event Log (baris baru, urutan default `Date` terbaru)
12. Tutup modal Event Log
13. Buka Approvals > Tab History

### TC-AC-ACTS-709: Distributor Suspended, permintaan tulis ditolak server

14. Ganti sesi API ke Distributor dengan entitas Suspended (`distributorSuspended_automated_{namaCompany}@qwertysystem.net`)
15. Catat baseline jumlah unit SKU
16. Kirim request Add Stock, Audit, dan Delete langsung
17. Verifikasi semua request ditolak server
18. Verifikasi baca tetap diizinkan (request baca daftar unit berhasil)

### TC-AC-ACTS-784: Read Only, request tulis langsung (Add Stock, Audit, Delete) ditolak server

19. Ganti sesi API ke Read Only (`readOnly_automated_{namaCompany}@qwertysystem.net`)
20. Catat baseline jumlah unit Available dan statusnya
21. Kirim request Add Stock, Audit Submit, dan Delete langsung ke endpoint
22. Verifikasi semua request ditolak server dan tidak diproses
23. Verifikasi tidak ada unit dibuat, diubah status, atau dihapus (sama dengan baseline)

### TC-AC-ACTS-785: Manage TAG stock dengan capability parsial, request di luar capability ditolak server

24. Ganti sesi API ke Manage TAG stock Read+Create (`manageTagStockCreate_automated_{namaCompany}@qwertysystem.net`)
25. Catat baseline jumlah unit Available dan statusnya
26. Kirim request Audit Submit dan Delete langsung
27. Verifikasi kedua request ditolak server dan tidak diproses
28. Ganti sesi API ke Manage TAG stock Read+Update (`manageTagStockUpdate_automated_{namaCompany}@qwertysystem.net`)
29. Kirim request Add Stock dan Delete langsung
30. Verifikasi kedua request ditolak server dan tidak diproses
31. Ganti sesi API ke Manage TAG stock Read+Delete (`manageTagStockDelete_automated_{namaCompany}@qwertysystem.net`)
32. Kirim request Add Stock dan Audit Submit langsung
33. Verifikasi kedua request ditolak server dan tidak diproses
34. Verifikasi tidak ada perubahan data (sama dengan baseline)

### TC-AC-ACTS-786: Pemegang Manage TAG stock Update yang bukan Total Control atau Additional Approver tidak dapat Approve atau Reject

35. Ganti sesi API ke Manage TAG stock Read+Update (`manageTagStockUpdate_automated_{namaCompany}@qwertysystem.net`)
36. Kirim request Approve langsung lalu request Reject langsung atas Subject Register Duplicate pending
37. Verifikasi kedua request ditolak server dan tidak diproses
38. Verifikasi Subject tetap pending
39. Verifikasi tidak ada TAG Code diterbitkan

## Notes

- Mode: FE+BE. Spec ini melewati sekitar 35 langkah (39 langkah); alasan: semua blok satu kelas defense-in-depth (request langsung ke server) dengan satu dataset, dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; ganti sesi API per akun dituntut TC-AC-ACTS-709, TC-AC-ACTS-784, TC-AC-ACTS-785, dan TC-AC-ACTS-786.
- Cara baca entri audit trail baru (S-12, S-14): jumlah entri dicatat sebelum aksi pemicu, selisihnya diverifikasi, lalu baris teratas urutan default `Date` terbaru dibaca; bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya. Pada TC-AC-ACTS-706 selisih satu baris, sehingga tidak ada entri semenit yang perlu diasersi sebagai himpunan.
- K-1: TC-AC-ACTS-709, TC-AC-ACTS-784, TC-AC-ACTS-785, dan TC-AC-ACTS-786 adalah TC defense-in-depth (kelas a) dengan Expected respons API; tetap masuk spec FE+BE dan hanya mengasersi status respons dan state data (8b butir 1). P-5 butir (b): TC-AC-ACTS-709 adalah satu TC objek-uji ringan kelas h (state tenant, write-lockdown Suspended) tanpa harness eksternal; jumlah TC objek-uji ringan kelas h dalam spec ini satu.
- TC-AC-ACTS-706 adalah satu-satunya blok UI: payload dikirim lewat dialog Review (Total Control), bukan request langsung.
- Langkah penghubung tanpa Verifikasi (S-03): langkah ganti sesi API (langkah 14 sampai 35; ganti akun punya langkah eksplisit, S-07), mencatat baseline (S-12), "Tunggu aksi selesai" sesudah `[Submit]` sebelum membuka Event Log (bagian 8b butir 8), dan membuka layar. Urutan TC: TC-AC-ACTS-786 sesudah TC-AC-ACTS-785 memakai sesi Read+Update yang sama dengan langkah ganti sesi eksplisit (S-10). Langkah "Tutup modal Event Log" menutup modal sebelum pindah surface atau ganti akun (pemulihan state, S-09).
- Temuan untuk QA:
  - TC-AC-ACTS-706 menyebut "Event Log" untuk tampilan teks Approval Note tanpa menyebut tab dan baris; spec mengasersi baris pembanding lalu teks payload di modal Event Log.
  - TC-AC-ACTS-709 menyebut ACC "Distributor (entitas Suspended)" dengan Pre-setup #20; pembatasan paket dan state tenant lain ada di spec state tenant.
  - TC-AC-ACTS-785 menyebut "ulangi untuk Read+Update dan Read+Delete" dengan satu unit Available; spec memakai satu baseline untuk ketiga sesi.
