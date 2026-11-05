---
id: TC-FA-RP-E2E-391-baris-pola-gm-role-transaksi-tidak-dikecualikan-hanya-di-dalam-constraint
title: "Baris pola Group Manager Role Transaksi tidak dikecualikan dari gate: penugasan di dalam constraint menulis baris pola hanya di dalam constraint"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1237
coverage:
  web: automated
---

# Baris pola Group Manager Role Transaksi tidak dikecualikan dari gate: penugasan di dalam constraint menulis baris pola hanya di dalam constraint

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Spec ini tidak berganti akun.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #17 (Gunawan Halim, Home Group `Data Center`), #18 (pohon Group: `Head Office` > `IT Infrastructure` > `Data Center` > `Rack A1`; `IT Infrastructure` > `Helpdesk`), #19 (baris pola Role Transaksi pada setiap node dan sub-tab: Asset Admin dan Approver untuk Admin Utama, Siti Rahmawati, dan Rina Wulandari; seed manual hanya pada `IT Infrastructure` sub-tab `Disposal`), #2 (aktor).
- Seeding precondition TC (hook `before`, dipakai sebagai precondition, tidak diasersi): Gunawan Halim berstatus Standard tanpa penugasan Group Manager dan tanpa penugasan Role Transaksi; Home Group tetap `Data Center` sesuai Pre-setup #17. Kemampuan seed dan pemulihan Pre-setup #17 adalah fixture backend yang disediakan tim FE/BE, tanpa endpoint karangan.
- Data Dinamis: tidak ada data yang dibuat spec.
- State yang diubah dan pemulihannya: langkah 5 menjadikan Gunawan Halim Group Manager di `Data Center` dan menulis baris pola Role Transaksi (Asset Admin dan Approver). Hook `after` melepas penugasan Group Manager Gunawan Halim beserta baris pola-nya lalu memulihkan Pre-setup #17 lewat fixture backend yang disediakan tim FE/BE, tidak berasumsi langkah spec berhasil penuh. Entri Changelog bersifat permanen. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1237: Baris pola GM Role Transaksi tidak dikecualikan dari gate: hanya di dalam constraint

1. Klik Tab `Group Manager`
2. Klik `[+ Assign]` di Tab Group Manager
3. Pilih group `Data Center` pada field Group
4. Ketik Search `Gunawan Halim`, tekan Enter
5. Centang Gunawan Halim lalu klik `[Assign]`
6. Tunggu aksi selesai: popup Assign tertutup
7. Ketik Search `Gunawan Halim`, tekan Enter
8. Verifikasi baris Gunawan Halim dengan Group `Data Center` tampil di Tab Group Manager
9. Klik `(←)` pada kotak Search
10. Klik Tab `Transaction Role`, klik node `Data Center` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
11. Verifikasi baris pola GM Gunawan Halim tampil di section Asset Admin `Data Center`
12. Verifikasi baris pola GM Gunawan Halim tampil di section Approver `Data Center`
13. Klik node `Rack A1` di Sidebar Group Tree
14. Verifikasi baris pola GM Gunawan Halim tampil di section Asset Admin `Rack A1`
15. Verifikasi baris pola GM Gunawan Halim tampil di section Approver `Rack A1`
16. Klik node `Helpdesk` di Sidebar Group Tree
17. Verifikasi sedikitnya satu baris lain tampil di section Asset Admin dan di section Approver `Helpdesk`
18. Verifikasi tidak ada baris Gunawan Halim di section Asset Admin dan Approver `Helpdesk`
19. Klik node `IT Infrastructure` di Sidebar Group Tree
20. Verifikasi sedikitnya satu baris lain tampil di section Asset Admin dan di section Approver `IT Infrastructure`
21. Verifikasi tidak ada baris Gunawan Halim di section Asset Admin dan Approver `IT Infrastructure`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 21 langkah, di bawah batas sekitar 35.
- Langkah penghubung (S-03): langkah 1 sampai 3 (membuka Tab dan popup Assign, memilih group), langkah 6 (tunggu aksi selesai, bagian 8b butir 8), langkah 9 (membersihkan Search), langkah 10, 13, 16, dan 19 (navigasi Tab, node, dan sub-tab; sub-tab `Disposal` diasumsikan tetap terpilih saat berpindah node, mengikuti TC yang hanya menyebut "klik node"). Langkah 4 adalah Search nama kandidat di Table User Picker (R-16, R-22); langkah 7 adalah Search untuk menemukan baris target di Tab Group Manager (R-16).
- Anchor positif absence (bagian 8b butir 2): baris Gunawan Halim di Tab Group Manager (langkah 8) dan baris pola di `Data Center` dan `Rack A1` (langkah 11, 12, 14, 15) membuktikan penugasan dan penulisan baris pola; langkah 17 dan 20 (baris lain, yaitu baris pola Total Control dan seed Pre-setup #19, tampil di kedua section pada node yang sama) mendahului absence langkah 18 dan 21.
- Tanpa Search pada tabel Role Transaksi: precondition TC hanya memuat Pre-setup #17, #18, dan #19 sehingga tiap section pada keempat node memuat paling banyak tujuh baris dalam satu halaman.
- Temuan untuk QA:
  - TC-FA-RP-1237 bergantung pada FARP-LOGIC-16g dan FARP-LOGIC-04b yang belum dikonfirmasi PM (Open Item #9 / NC-20). Spec mengikuti TC apa adanya: baris pola GM tampil pada `Data Center` dan `Rack A1` dan tidak ada pada `Helpdesk` maupun `IT Infrastructure`. Bila PM menetapkan lain (mis. baris pola GM dikecualikan dari gate, atau penulisan mengikuti cakupan node di luar constraint), Expected b dan c usang. Asersi tidak diperlebar ke hal yang belum diputuskan (tanpa asersi toast Assign, tanpa jumlah entri Changelog, dan tanpa asersi jumlah baris).
  - TC-FA-RP-1237 Expected a menyebut "penugasan Group Manager tersimpan di `Data Center`" tanpa teks toast; spec mengasersi baris Gunawan Halim dengan Group `Data Center` di Tab Group Manager (langkah 8) dan tidak mengasersi toast.
  - Email akun login Gunawan Halim tidak tertulis di Pre-setup #17. Spec ini tidak login sebagai Gunawan Halim (aktor Total Control), sehingga `FA_GUNAWAN_PASSWORD` tidak dipakai.
  - Pre-setup #17 tidak menyebut tingkat akses Gunawan Halim; precondition d TC menyebut tanpa penugasan Group Manager, dan spec memakai seeding sesuai precondition itu.
  - Post Condition TC kosong ("-").
