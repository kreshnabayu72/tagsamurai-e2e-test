---
id: TC-FA-SU-E2E-070-modal-assign-transaction-role-ganti-transaction-label-group-dan-popup-tree-group
title: "Modal Assign Transaction Role: Ganti Transaction, Label Group, dan Popup Tree Group"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-233
  - TC-FA-SU-234
  - TC-FA-SU-235
coverage:
  web: automated
---

# Modal Assign Transaction Role: Ganti Transaction, Label Group, dan Popup Tree Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21: Finance & Accounting dengan anak Accounts Payable, IT Infrastructure, dan grup lain) dan Transaction Role (Pre-setup #39).
- Pengguna target: Mira Anggraini (Disposal × Staff dan Borrowing & Assignment × Approver pada Finance & Accounting) tanpa Home Group (Pre-setup #50 `FaUserNoHG`, varian `FaUserMain` dengan Home Group dikosongkan) agar pemilih Group tidak disaring gate Home Group (FI-32, Catatan TC).
- Data uji: Group IT Infrastructure, Transaction Disposal lalu Transfer, Role Asset Admin (TC-FA-SU-233); Group Finance & Accounting dan IT Infrastructure (TC-FA-SU-234); Group Finance & Accounting (TC-FA-SU-235).
- State global yang diubah: tidak ada data yang disimpan; isian modal dibuang lewat `[Leave]`.
- Target tanpa Home Group (Pre-setup #50, `FaUserNoHG`; Catatan TC: TC penugasan Tab Role yang memilih node bebas dijalankan pada varian tanpa Home Group, FI-32), diterapkan per target: Home Group Mira Anggraini (Finance & Accounting pada Pre-setup #43) dikosongkan lewat seed API di hook `before` supaya node di luar constraint tidak Disabled oleh gate Home Group; Home Group Mira Anggraini dipulihkan ke Finance & Accounting di hook `after`. Seed per target disediakan tim FE/BE.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-233: Mengganti Transaction setelah Role terisi mengosongkan Role dan mengunci ulang field Role

1. Ketik Search `Mira Anggraini`, tekan Enter, lalu buka Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role lalu klik `[+ Assign]`
2. Pilih Group IT Infrastructure, Transaction Disposal, dan Role Asset Admin
3. Verifikasi Role terisi `Asset Admin` untuk Transaction Disposal
4. Ganti Transaction ke Transfer
5. Verifikasi Role kosong
6. Verifikasi field Role Enabled kembali dengan opsi sesuai katalog Transfer (Asset Admin, Monitoring & Report, dan Approver)

### TC-FA-SU-234: Label tombol Group: Select Group, 1 Group selected, dan N Groups selected

7. Klik `[Clear Field]` untuk mengosongkan isian modal
8. Verifikasi tombol Group berlabel `Select Group` selama belum ada pilihan
9. Klik tombol Group, centang Finance & Accounting, klik `[Select]`
10. Verifikasi tombol Group berlabel `1 Group selected`
11. Klik tombol Group, centang IT Infrastructure, klik `[Select]`
12. Verifikasi tombol Group berlabel `2 Groups selected`
13. Klik tombol Group, hapus semua centang, klik `[Select]`
14. Verifikasi tombol Group berlabel `Select Group`

### TC-FA-SU-235: Popup tree Group pada modal: confirm footer, perubahan pending sampai Select, dan tanpa node Disabled already assigned

15. Klik tombol Group
16. Verifikasi popup tree berisi Search `Search groups...`, pohon grup, dan footer `[Cancel]` (Text, Contrast) serta `[Select]`
17. Verifikasi node yang sudah ter-assign pada kombinasi lain tidak Disabled karena Group dipilih sebelum Transaction dan Role
18. Verifikasi node yang ancestor atau descendant-nya sudah memegang role (Accounts Payable sebagai descendant dari Finance & Accounting yang ter-assign) tidak Disabled (overlap diizinkan)
19. Verifikasi tidak ada node Disabled karena constraint Home Group: seluruh node pohon tampil tanpa tooltip penyaringan (target tanpa Home Group, Pre-setup #50; gate TC-FA-SU-1117)
20. Centang node Finance & Accounting
21. Verifikasi node anak Accounts Payable tidak ikut tercentang (tanpa cascade parent ke child)
22. Klik `[Cancel]`
23. Verifikasi tombol Group tetap berlabel `Select Group` (centang dibuang)
24. Klik tombol Group, centang Finance & Accounting, klik `[Select]`
25. Verifikasi tombol Group berlabel `1 Group selected` (centang berlaku setelah `[Select]`)
26. Klik `[✕]` pada modal
27. Verifikasi dialog `Unsaved Changes`
28. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 7 dan 26 sampai 28. `[Clear Field]` memulihkan isian TC-FA-SU-233 sebelum TC-FA-SU-234 mengandalkannya (S-09); penutupan modal dirty mengikuti S-08.
- Modal Assign Transaction Role dibuka sekali pada TC-FA-SU-233 dan dipakai TC-FA-SU-234 dan 235 tanpa dibuka ulang (halaman yang sama dipakai berulang, bagian 3 prinsip 13); tombol Group kembali `Select Group` pada akhir TC-FA-SU-234 sehingga TC-FA-SU-235 mulai dari keadaan awal.
- Langkah penghubung Search (S-03): Search nama pengguna target pada langkah 1 digabung ke langkah pembuka Detail atau pembacaan baris, untuk menemukan baris target di User List yang memuat 25 pengguna pada 3 halaman (R-16, bagian 8b butir 13); langkah berikutnya mengganti isi kotak search yang masih berisi nama sebelumnya (bagian 8b butir 9).
- Temuan untuk QA:
  - TC-FA-SU-233 butir b ("Field Role terkunci lalu Enabled kembali") tidak punya cara observasi keadaan terkunci sementara; spec mengasersi keadaan akhir Enabled dengan opsi katalog Transfer.
  - TC-FA-SU-235 butir c diperbarui (E-FASU-38): node ancestor atau descendant pemegang role juga tidak Disabled; spec menambah satu Verifikasi dengan Accounts Payable (descendant Finance & Accounting yang dipegang Mira Anggraini). TC tidak menyebut kasus ancestor; kasus itu tidak diasersi di spec ini (lihat TC-FA-SU-1104, spec E2E-411).
  - TC-FA-SU-235 butir c diperbarui lagi (gate Home Group, FI-32): "tanpa node Disabled" kini hanya berlaku untuk target tanpa Home Group; spec memakai Mira Anggraini pada Pre-setup #50 dan menambah satu Verifikasi (langkah 19). Gate pada target ber-Home Group diuji TC-FA-SU-1117.
  - TC-FA-SU-235 butir c tidak menyebut node mana yang ter-assign pada kombinasi lain; spec mengasersi node yang sudah ter-assign pada Mira Anggraini (Finance & Accounting) tidak Disabled.
