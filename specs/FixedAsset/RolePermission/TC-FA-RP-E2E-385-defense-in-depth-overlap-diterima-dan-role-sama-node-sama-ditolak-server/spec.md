---
id: TC-FA-RP-E2E-385-defense-in-depth-overlap-diterima-dan-role-sama-node-sama-ditolak-server
title: "Defense-in-depth: Assign Role Transaksi tumpang tindih ancestor dan descendant diterima server, role sama pada node sama ditolak"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-1224
coverage:
  web: automated
---

# Defense-in-depth: Assign Role Transaksi tumpang tindih ancestor dan descendant diterima server, role sama pada node sama ditolak

## Prerequisites

- Mode: FE+BE.
- Akun aktor (sesi API aktor, bukan sesi UI): Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Sesi UI dibuka di hook `before` spec ini; halaman dibuka hook `beforeEach` suite dan tidak dipakai langkah. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #15 (kolam pengguna Standard), #18 (pohon Group), #19 (seed Role Transaksi pada `IT Infrastructure` sub-tab `Disposal`: Asset Admin Nadia Putri dan Monitoring & Report Oscar Pratama).
- Seeding precondition (hook `before`, lewat fixture BE yang disediakan tim FE/BE, tanpa endpoint karangan): Nadia Putri dan Oscar Pratama tanpa penugasan di `Data Center` sub-tab `Disposal` (penugasan yang tersisa dicabut). Spec tidak membuat data Dinamis.
- Kemampuan teknis: request langsung ke server (bukan lewat UI) dikirim lewat klien HTTP yang disediakan tim FE/BE memakai sesi API aktor (`suite.md`, Hook suite); endpoint tidak disebut karena tidak ada di TC. State data dibaca dan dipulihkan lewat fixture BE (disediakan tim FE/BE). Asersi hanya status respons, pesan respons, dan state data (bagian 8b butir 1).
- Baseline (S-12): penugasan Role Transaksi `IT Infrastructure` sub-tab `Disposal` (Nadia Putri Asset Admin dan Oscar Pratama Monitoring & Report) dicatat lewat fixture BE sebelum request pertama.
- State yang diubah dan pemulihannya: dua request pertama menambah penugasan Asset Admin Nadia Putri dan Oscar Pratama pada `Data Center` sub-tab `Disposal`. Keduanya dicabut pada langkah terakhir spec dan di hook `after` sebagai cadangan, lewat fixture BE, sehingga `Data Center` kembali ke Pre-setup #19 (tanpa baris manual). Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md` bagian "Env password akun aktor". Password dan token tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1224: Assign tumpang tindih ancestor dan descendant diterima server, role sama pada node sama ditolak

1. Catat baseline (aksi tanpa `Verifikasi`): penugasan Role Transaksi `IT Infrastructure` sub-tab `Disposal` (Nadia Putri Asset Admin, Oscar Pratama Monitoring & Report) lewat fixture BE
2. Kirim request langsung ke server (bukan lewat UI) untuk meng-Assign Nadia Putri sebagai Asset Admin pada `Data Center` sub-tab `Disposal`
3. Verifikasi respons sukses
4. Kirim request langsung ke server (bukan lewat UI) untuk meng-Assign Oscar Pratama sebagai Asset Admin pada `Data Center` sub-tab `Disposal`
5. Verifikasi respons sukses
6. Verifikasi lewat fixture BE Nadia Putri dan Oscar Pratama tersimpan sebagai Asset Admin pada `Data Center` sub-tab `Disposal`
7. Verifikasi lewat fixture BE baris `IT Infrastructure` (Nadia Putri Asset Admin dan Oscar Pratama Monitoring & Report) tetap ada
8. Kirim ulang request langkah 2 (bukan lewat UI)
9. Verifikasi respons status `422` dengan pesan `Nadia Putri is no longer eligible. Please select another.`
10. Verifikasi lewat fixture BE Nadia Putri dan Oscar Pratama masing-masing satu baris Asset Admin di `Data Center`
11. Verifikasi lewat fixture BE penugasan `IT Infrastructure` sub-tab `Disposal` sama dengan baseline langkah 1 (tidak berubah)
12. Pulihkan lewat fixture BE: cabut baris Asset Admin Nadia Putri dan Oscar Pratama pada `Data Center` sub-tab `Disposal`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 12 langkah.
- `K-1` (TC defense-in-depth dengan Expected respons API): TC kelas a ini tetap masuk spec FE+BE walau tumpang tindih dengan TC backend karena TC granular tetap sumber dan tiap TC tepat satu spec; Expected berupa status respons `422`, pesan respons, dan state data lewat fixture BE (BE mencatatnya pada tingkat endpoint). Spec berdiri sendiri (kelas a) dan tidak digabung dengan spec defense-in-depth lain.
- Bagian 8b butir 1: seluruh langkah "Kirim request langsung" tidak melewati browser; pengalihan halaman, toast, atau tampilan tidak diasersi di spec ini. Perilaku FE untuk respons yang sama tidak ditulis.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 1 (baseline, S-12) dan langkah 12 (pemulihan, S-09). Satu `Verifikasi` per request (R-03) untuk langkah 3, 5, dan 9; status respons dan pesan respons langkah 9 satu respons.
- Pembagian klausa Expected a: respons sukses diasersi per request (langkah 3 dan 5), penyimpanan kedua penugasan pada `Data Center` (langkah 6), dan baris `IT Infrastructure` tidak terhapus (langkah 7) masing-masing satu `Verifikasi` (S-01). Klausa c: langkah 10 dan 11. Frasa dalam kurung pada Expected a ("tanpa node disabled dan tanpa penyaringan redundansi") adalah penjelasan perilaku UI dan tidak diasersi (bagian 8b butir 1).
- Asersi "tidak ada baris atau entri log baru" atas penolakan langkah 9 tidak diasersi di spec ini (S-05; TC tidak memuatnya).
- Temuan untuk QA:
  - Asumsi status `422` dan pesan `Nadia Putri is no longer eligible. Please select another.` bergantung pada backend (K-1; pesan disebut TC sebagai copy `V-09`); bila backend memakai kode atau teks lain, TC-source perlu ditinjau.
  - TC-FA-RP-1224 tidak menyebut endpoint dan body request; spec tidak mengarangnya (klien HTTP dan fixture BE disediakan tim FE/BE).
  - TC-FA-RP-1224 menargetkan `Data Center` (Pre-setup #18 bersama) sebagai tujuan penulisan (S-06). Spec memulihkan baris hasil request lewat fixture BE (langkah 12 dan hook `after`) dan Prerequisites menyatakan efeknya; bila auditor menilai target harus data milik spec, pindahkan ke Group sementara bersuffix `{runId}-385`.
  - TC-FA-RP-1224 Precondition tidak menyebut bahwa Nadia Putri dan Oscar Pratama belum punya penugasan di `Data Center`; spec menetapkannya lewat seeding hook `before`.
  - TC-FA-RP-1224 Expected a menyebut "respons sukses" tanpa kode status; spec tidak mengarang kode.
  - Post Condition TC-FA-RP-1224 kosong ("-").
