---
id: TC-FA-RP-E2E-276-defense-in-depth-penolakan-server-atas-permintaan-langsung-8
title: "Defense-in-depth: penolakan server atas permintaan langsung (8/9)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-959
  - TC-FA-RP-960
  - TC-FA-RP-962
  - TC-FA-RP-1038
  - TC-FA-RP-1045
  - TC-FA-RP-1098
  - TC-FA-RP-1125
coverage:
  web: automated
---

# Defense-in-depth: penolakan server atas permintaan langsung (8/9)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`), password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (Ahmad Fauzi memegang `Manage accounting` dengan Create nonaktif dan Read aktif; `Import data` dengan Delete tidak berlaku), #6 (Hendra Wijaya memegang Global Role `Manage user & role`; TC-FA-RP-1045), #17 (Hesti Rahma: Home Group `Logistics Warehouse`), #18 (pohon group Company Alpha), #19 (seed Role Transaksi Disposal pada `IT Infrastructure`: Nadia Putri, Oscar Pratama, Putri Wulandari, Pandu Wijaya), dan #20 (Approval Scope `Transfer` pada `IT Infrastructure` bernilai `Both`).
- Kemampuan teknis: TC-FA-RP-962 memakai UI (Search di Tab Total Control) dan bukan request langsung; pemulihan nilai Create `Manage accounting` dan `Import data` Ahmad Fauzi di hook `after`.
- Request langsung ke server (bukan lewat UI) dikirim lewat klien HTTP yang disediakan tim FE/BE memakai sesi API aktor (`suite.md`); endpoint tidak disebut karena tidak ada di TC. State data diperiksa lewat fixture BE (kemampuan disediakan tim FE/BE). Asersi hanya status respons dan state data (bagian 8b butir 1).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `Fixture.fixedAssetRolePermission` (berkas `fixtures/fixedAssetRolePermission.json`, belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung; data Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after`. Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`). Nilai awal baris yang diasersi "tidak berubah" di-seed deterministik (dicatat di Data Pre-setup spec ini).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-959: Server mengabaikan nilai Read dari klien tanpa error

1. Kirim request langsung ke server (bukan lewat UI) untuk mengubah Create menjadi aktif dengan Read=false pada baris Ahmad Fauzi `Manage accounting`
2. Verifikasi respons status `200`
3. Verifikasi lewat fixture BE Create aktif tersimpan pada baris Ahmad Fauzi `Manage accounting`
4. Verifikasi lewat fixture BE Read tetap aktif (nilai Read dari klien diabaikan)

### TC-FA-RP-960: Server mengabaikan flag kolom yang tidak berlaku pada role tersebut

5. Kirim request langsung ke server (bukan lewat UI) untuk mengubah Create=true dan Delete=true pada baris Ahmad Fauzi di `Import data` (Delete tidak berlaku)
6. Verifikasi respons status `200`
7. Verifikasi lewat fixture BE Create aktif tersimpan pada baris Ahmad Fauzi di `Import data`
8. Verifikasi lewat fixture BE Delete tetap tidak aktif tanpa error

### TC-FA-RP-1038: Assign Group Manager di luar Home Group constraint ditolak server

9. Kirim request langsung ke server (bukan lewat UI) untuk meng-Assign Hesti Rahma (Home Group `Logistics Warehouse`) sebagai Group Manager di `Data Center`
10. Verifikasi respons status `422` dengan pesan `Hesti Rahma is no longer eligible. Please select another.` (copy `V-09`, tanpa copy khusus Home Group constraint)
11. Verifikasi lewat fixture BE tidak ada penugasan Group Manager baru

### TC-FA-RP-1045: Assign Group Role Manage user & role ke user ber-Global Role aktif lewat request langsung ditolak server

12. Kirim request langsung ke server (bukan lewat UI) untuk meng-Assign Hendra Wijaya ke Group Role `Manage user & role` di `IT Infrastructure`
13. Verifikasi respons status `422` dengan pesan `Hendra Wijaya is no longer eligible. Please select another.`
14. Verifikasi lewat fixture BE tidak ada baris baru pada Detail Role `Manage user & role`

### TC-FA-RP-1098: Radio Approval Scope di luar enum ditolak validasi skema

15. Kirim request langsung ke server (bukan lewat UI) untuk menyimpan Approval Scope `Transfer` pada `IT Infrastructure` dengan nilai `sideways`
16. Verifikasi respons status `422`
17. Verifikasi lewat fixture BE Approval Scope `Transfer` pada `IT Infrastructure` tetap `Both`

### TC-FA-RP-1125: Assign Role Transaksi untuk user yang sudah memegang role yang sama ditolak server

18. Kirim request langsung ke server (bukan lewat UI) untuk meng-Assign Nadia Putri sebagai Asset Admin, Oscar Pratama sebagai Monitoring & Report, Putri Wulandari sebagai Staff, dan Pandu Wijaya sebagai Approver pada `IT Infrastructure` sub-tab Disposal (empat request)
19. Verifikasi respons status `422` pada keempat request dengan pesan `Nadia Putri is no longer eligible. Please select another.`, `Oscar Pratama is no longer eligible. Please select another.`, `Putri Wulandari is no longer eligible. Please select another.`, dan `Pandu Wijaya is no longer eligible. Please select another.` (copy `V-09`, tanpa copy khusus role yang sama)
20. Verifikasi lewat fixture BE tidak ada penugasan baru dan penugasan lama tidak berubah

### TC-FA-RP-962: Input Search dicocokkan sebagai teks biasa

21. Klik ikon Search di Tab Total Control
22. Ketik Search `<script>alert(1)</script>`, tekan Enter
23. Verifikasi kata kunci dicocokkan sebagai teks biasa: markup tidak diinterpretasi dan tidak ada skrip yang dijalankan
24. Verifikasi tabel menampilkan empty state `No results found`
25. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 25 langkah.
- `K-1` (TC defense-in-depth dengan Expected respons API): TC kelas a ini tetap masuk spec FE+BE walau tumpang tindih dengan TC backend karena TC granular tetap sumber dan tiap TC tepat satu spec; Expected berupa status respons dan state data lewat fixture BE (BE mencatatnya pada tingkat endpoint).
- Langkah penghubung (S-03): ganti akun (bila ada) dan pencatatan state awal. Seluruh langkah "Kirim request langsung" tidak melewati browser; perilaku FE untuk respons yang sama tidak diasersi di spec ini (bagian 8b butir 1).
- TC-FA-RP-962 (XSS pada Search, kelas a defense-in-depth) dijalankan lewat UI karena langkah TC memakai ikon Search; asersinya perilaku UI atas input, bukan respons server.
- TC-FA-RP-1098 Expected b menyebut juga "tidak ada entri log"; asersi itu ada di spec 292 (Absence log: permintaan langsung yang ditolak; aksi nyata dengan baseline sendiri, S-05). Spec ini hanya mengasersi status `422` dan nilai Approval Scope tetap `Both`. Copy `(copy usulan, PRD 12 #1)` pada TC-FA-RP-1038, 1045, dan 1125 diasersi literal sesuai TC dan bergantung pada persetujuan PM.
- Temuan untuk QA:
  - TC-FA-RP-959 dan 960 menulis "Respons status `200`" tanpa pesan; spec mengasersi status dan state data. TC-FA-RP-1125 memuat empat pesan dalam satu Expected a; spec mengasersi empat request dengan pesan masing-masing dalam satu Verifikasi (butir Expected yang sama).
  - TC-FA-RP-1038 dan 1045 tidak menyebut aktor selain Total Control; Precondition TC-FA-RP-1045 merujuk Pre-setup #6 (Hendra Wijaya) sebagai target dan #18 sebagai group. Post Condition kosong pada seluruh TC.
