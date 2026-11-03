---
id: TC-AC-ACTS-E2E-102-approvals-duplicate-e4-additional-approver-subject-sendiri-disembunyikan
title: "Approvals Duplicate: E4 Additional Approver, Subject Sendiri Tersembunyi di Tab Active, Tampil di Tab History, Approve Langsung Ditolak, dan Activation Collision Tanpa E4"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACTS-287
  - TC-AC-ACTS-288
  - TC-AC-ACTS-289
  - TC-AC-ACTS-768
  - TC-AC-ACTS-806
coverage:
  web: automated
---

# Approvals Duplicate: E4 Additional Approver, Subject Sendiri Tersembunyi di Tab Active, Tampil di Tab History, Approve Langsung Ditolak, dan Activation Collision Tanpa E4

## Prerequisites

- Mode: FE+BE. Request langsung ke server pada TC-AC-ACTS-288 (klien HTTP, kelas a ringan, K-1).
- Akun aktor: Additional Approver dengan capability Manage TAG stock Create `additionalApproverCreate_automated_{namaCompany}@qwertysystem.net` (Pre-setup #21), password dari `Spectra.env.AC_AA_CREATE_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun ganti di tengah spec: Total Control Principal `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Pergantian akun ditulis sebagai langkah eksplisit.
- Akun ganti di tengah spec: Additional Approver tanpa capability `additionalApprover_automated_{namaCompany}@qwertysystem.net` (Pre-setup #4), password dari `Spectra.env.AC_AA_PASSWORD`. Pergantian akun ditulis sebagai langkah eksplisit.
- Halaman awal spec: Approvals > TAG Stock > Tab Active (dibuka langkah 1).
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- Data Subject pending disiapkan seeding fixture BE (disediakan tim FE/BE; ada Total Control lain sebagai approver): Subject S1 buatan Additional Approver (`additionalApproverCreate`) untuk TC-AC-ACTS-287 dan TC-AC-ACTS-768; Subject S2 buatan Distributor; Subject S1b buatan Additional Approver yang diputuskan Total Control pada TC-AC-ACTS-806; Subject S1c buatan Additional Approver untuk request Approve langsung (TC-AC-ACTS-288); Subject Activation Collision pending dari Client (TC-AC-ACTS-289). Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script.
- Kemampuan teknis disediakan tim FE/BE: klien HTTP untuk request Approve langsung dan kemampuan baca status Subject dan TAG Code (fixture BE); asersi TC-AC-ACTS-288 hanya status respons dan state data (8b butir 1).
- Email akun TC-AC-ACTS-289 tidak tertulis eksplisit di Pre-setup TC (lihat Temuan untuk QA); spec memakai Pre-setup #4 Additional Approver tanpa capability.
- Env var password akun aktor: `Spectra.env.AC_AA_CREATE_PASSWORD`, `Spectra.env.AC_TC_PASSWORD`, `Spectra.env.AC_AA_PASSWORD`. Password tidak ditulis di spec atau fixture. Nama `AC_AA_CREATE_PASSWORD`, `AC_AA_PASSWORD` adalah nama baru yang didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-287: E4, Subject buatan Additional Approver sendiri disembunyikan dari Tab Active miliknya

1. Buka Approvals > TAG Stock > Tab Active
2. Verifikasi Tab Active memuat Subject buatan pihak lain (S2)
3. Cari baris Subject buatan sendiri (S1)
4. Verifikasi baris S1 tidak muncul sama sekali di Tab Active (Hidden)
5. Verifikasi tidak ada row action `Review` untuk S1

### TC-AC-ACTS-768: Additional Approver, Subject buatan sendiri tersembunyi di Tab Active, Subject pihak lain dan tampilan Total Control tetap lengkap

6. Cari S1 dan S2 di Tab Active
7. Verifikasi S1 tidak muncul sebagai baris
8. Verifikasi S2 muncul dengan row action `Review`
9. Ganti akun: klik Logout
10. Login sebagai Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`)
11. Buka Approvals > TAG Stock > Tab Active
12. Cari S1 dan S2
13. Verifikasi S1 dan S2 sama-sama muncul

### TC-AC-ACTS-806: Subject buatan sendiri tidak tampil di Tab Active tetapi tampil di Tab History setelah diputuskan

14. Ganti akun: klik Logout
15. Login sebagai Additional Approver dengan capability Create (`additionalApproverCreate_automated_{namaCompany}@qwertysystem.net`)
16. Buka Approvals > TAG Stock > Tab Active dan cari S1b
17. Verifikasi S1b tidak muncul di Tab Active
18. Ganti akun: klik Logout
19. Login sebagai Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`)
20. Buka Approvals > TAG Stock > Tab Active, klik `Review` pada S1b
21. Pilih Approve, klik `[Submit]`
22. Tunggu aksi selesai (dialog Review tertutup)
23. Ganti akun: klik Logout
24. Login sebagai Additional Approver dengan capability Create (`additionalApproverCreate_automated_{namaCompany}@qwertysystem.net`)
25. Buka Approvals > TAG Stock > Tab History dan cari S1b
26. Verifikasi S1b tampil di Tab History dengan Approval `Approved`, Approver nama Total Control, dan TAG Code terisi
27. Klik (⋯) > `Detail` pada baris S1b
28. Verifikasi Dialog Detail Approval versi read-only dengan footer `[Close]`
29. Klik `[Close]`

### TC-AC-ACTS-288: E4, request approve langsung atas Subject sendiri ditolak server

30. Kirim request Approve langsung ke server atas Subject S1c milik sendiri
31. Verifikasi server menolak request (konflik E4)
32. Verifikasi Subject S1c tetap pending
33. Verifikasi tidak ada TAG Code diterbitkan

### TC-AC-ACTS-289: E4 tidak berlaku untuk Activation Collision (requester selalu Client)

34. Ganti akun: klik Logout
35. Login sebagai Additional Approver tanpa capability (`additionalApprover_automated_{namaCompany}@qwertysystem.net`)
36. Buka Approvals > TAG Stock > Tab Active
37. Klik `Review` pada Subject Activation Collision pending
38. Pilih Approve, klik `[Submit]`
39. Verifikasi Approve berhasil karena pemohon adalah Client, bukan anggota pool (toast "Success, request has been approved.")

## Notes

- Mode: FE+BE. Spec ini melewati sekitar 35 langkah (39 langkah); alasan: semua blok satu halaman dan satu dataset Subject pending, dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; penggantian akun (Additional Approver, Total Control, Additional Approver tanpa capability) dituntut TC-AC-ACTS-768, TC-AC-ACTS-806, dan TC-AC-ACTS-289.
- K-1: TC-AC-ACTS-288 adalah TC defense-in-depth (kelas a) dengan Expected respons API; tetap masuk spec FE+BE dan hanya mengasersi status respons dan state data (8b butir 1). P-5 butir (b): TC-AC-ACTS-288 adalah satu TC objek-uji ringan kelas a tanpa harness eksternal dan tanpa state berat sendiri, berada di spec fungsional dengan permukaan sama (Approvals Tab Active).
- Urutan TC: TC-AC-ACTS-288 sebelum TC-AC-ACTS-289 supaya akun Additional Approver dengan capability Create tidak berganti dua kali; TC-AC-ACTS-806 memutuskan Subject (aksi yang mengubah data) sesudah TC-AC-ACTS-287 dan TC-AC-ACTS-768 yang hanya membaca (S-10). Urutan penulisan di atas mengikuti pengelompokan akun.
- Langkah penghubung tanpa Verifikasi (S-03): langkah ganti akun, "Tunggu aksi selesai" sesudah `[Submit]` Approve sebelum Logout (bagian 8b butir 8), buka layar, dan pencarian Subject. Pencarian S1 dan S2 adalah langkah penghubung menurut R-16.
- Absence S1 (Hidden) didahului anchor positif (Subject S2 buatan pihak lain tampil; 8b butir 2).
- Temuan untuk QA:
  - TC-AC-ACTS-289 menyebut ACC "Additional Approver" tanpa capability yang jelas; TC-AC-ACTS-287, TC-AC-ACTS-288, TC-AC-ACTS-768, dan TC-AC-ACTS-806 memakai capability Create (#21) dan TC-AC-ACTS-117 dan TC-AC-ACTS-132 tanpa capability (#4). Spec memakai #4.
  - TC-AC-ACTS-288 menyebut "konflik E4" tanpa kode status respons; spec mengasersi penolakan server tanpa angka status.
  - TC-AC-ACTS-287 menyebut "Ada Total Control lain" sebagai pool tanpa akun; disediakan seeding.
