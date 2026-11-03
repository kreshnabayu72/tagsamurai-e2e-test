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
- Pengguna target: Mira Anggraini (Disposal × Staff dan Borrowing & Assignment × Approver pada Finance & Accounting).
- Data uji: Group IT Infrastructure, Transaction Disposal lalu Transfer, Role Asset Admin (TC-FA-SU-233); Group Finance & Accounting dan IT Infrastructure (TC-FA-SU-234); Group Finance & Accounting (TC-FA-SU-235).
- State global yang diubah: tidak ada data yang disimpan; isian modal dibuang lewat `[Leave]`.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-233: Mengganti Transaction setelah Role terisi mengosongkan Role dan mengunci ulang field Role

1. Buka Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role lalu klik `[+ Assign]`
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
18. Centang node Finance & Accounting
19. Verifikasi node anak Accounts Payable tidak ikut tercentang (tanpa cascade parent ke child)
20. Klik `[Cancel]`
21. Verifikasi tombol Group tetap berlabel `Select Group` (centang dibuang)
22. Klik tombol Group, centang Finance & Accounting, klik `[Select]`
23. Verifikasi tombol Group berlabel `1 Group selected` (centang berlaku setelah `[Select]`)
24. Klik `[✕]` pada modal
25. Verifikasi dialog `Unsaved Changes`
26. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 7 dan 24 sampai 26. `[Clear Field]` memulihkan isian TC-FA-SU-233 sebelum TC-FA-SU-234 mengandalkannya (S-09); penutupan modal dirty mengikuti S-08.
- Modal Assign Transaction Role dibuka sekali pada TC-FA-SU-233 dan dipakai TC-FA-SU-234 dan 235 tanpa dibuka ulang (halaman yang sama dipakai berulang, bagian 3 prinsip 13); tombol Group kembali `Select Group` pada akhir TC-FA-SU-234 sehingga TC-FA-SU-235 mulai dari keadaan awal.
- Temuan untuk QA:
  - TC-FA-SU-233 butir b ("Field Role terkunci lalu Enabled kembali") tidak punya cara observasi keadaan terkunci sementara; spec mengasersi keadaan akhir Enabled dengan opsi katalog Transfer.
  - TC-FA-SU-235 butir c tidak menyebut node mana yang ter-assign pada kombinasi lain; spec mengasersi node yang sudah ter-assign pada Mira Anggraini (Finance & Accounting) tidak Disabled.
