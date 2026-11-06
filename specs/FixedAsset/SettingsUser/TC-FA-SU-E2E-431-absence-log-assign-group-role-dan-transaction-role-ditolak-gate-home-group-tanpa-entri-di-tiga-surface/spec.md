---
id: TC-FA-SU-E2E-431-absence-log-assign-group-role-dan-transaction-role-ditolak-gate-home-group-tanpa-entri-di-tiga-surface
title: "Absence Log: Permintaan Langsung Assign Group Role dan Assign Transaction Role yang Ditolak Gate Home Group Tidak Menulis Entri di Tab Changelog, Tab System Log Aktor, dan Activity Log"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-1116
  - TC-FA-SU-1122
coverage:
  web: automated
---

# Absence Log: Permintaan Langsung Assign Group Role dan Assign Transaction Role yang Ditolak Gate Home Group Tidak Menulis Entri di Tab Changelog, Tab System Log Aktor, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook suite dan sesi API aktor dinyatakan di `suite.md`.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), dan Pre-setup #51 (`FaUserHGT`, varian `FaUserMain` dengan Home Group tidak dikosongkan). Seed #51 belum tersedia dan disediakan tim FE/BE; dipulihkan lewat seed API di hook `before`.
- Target TC-FA-SU-1116: Gita Permata (Home Group Finance & Accounting). Grup di luar constraint: IT Infrastructure, Branch Surabaya. Grup dalam constraint: Accounts Payable. Group Role: Manage files.
- Target TC-FA-SU-1122: Gita Permata dan Vina Maharani (Home Group Jakarta Selatan Distribution Center, parent Region Jawa). Node di luar constraint: IT Infrastructure, Branch Surabaya, Region Jawa. Transaction Transfer, Role Monitoring & Report; baris Disposal × Asset Admin milik Gita Permata.
- Nilai nama pengguna, grup, dan penugasan dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): klien HTTP dengan token sesi API aktor (Total Control Lina Marlina) untuk permintaan langsung assign Group Role, assign Transaction Role, dan tambah grup ke baris Transaction Role; pembacaan jumlah entri Tab Changelog target, Tab System Log aktor, dan Activity Log FAMS sebelum aksi sebagai baseline (audit trail permanen: N tidak diturunkan dari seeding, bagian 8b butir 10).
- Jendela absence: "Tunggu 5 detik tanpa memuat ulang halaman" sebelum membaca surface log adalah pilihan spec (bukan nilai TC atau PRD). Tiap surface dibuka segar sehingga memuat data terkini.
- State global dan pemulihan: semua permintaan diharapkan ditolak sehingga penugasan tidak berubah. Bila ada yang diterima, penugasan dipulihkan ke Pre-setup #51 lewat seed API di hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-1116 (butir c, log): penolakan Assign Group Role tidak menulis entri log

1. Catat baseline: jumlah entri pada Tab Changelog Gita Permata, Tab System Log aktor (Lina Marlina), dan Activity Log FAMS
2. Kirim permintaan langsung ke API assign Group Role Manage files untuk Gita Permata dengan grup IT Infrastructure memakai klien HTTP dengan token sesi Lina Marlina
3. Verifikasi langkah 2 ditolak server dengan status 422 dan pesan copy `V-09` "Gita Permata is no longer eligible. Please select another."
4. Kirim permintaan langsung assign Group Role Manage files untuk Gita Permata dengan dua grup: Accounts Payable dan Branch Surabaya memakai klien HTTP dengan token sesi Lina Marlina
5. Verifikasi langkah 4 ditolak seluruhnya dengan status 422 dan pesan copy `V-09` "Gita Permata is no longer eligible. Please select another."
6. Tunggu 5 detik tanpa memuat ulang halaman
7. Ketik Search `Gita Permata`, tekan Enter, klik Name `Gita Permata`, lalu klik Tab Changelog
8. Verifikasi tabel Tab Changelog Gita Permata tampil
9. Verifikasi jumlah entri Tab Changelog Gita Permata sama dengan baseline langkah 1
10. Buka Settings > User lewat sidebar, ketik Search `Lina Marlina`, tekan Enter, klik Name `Lina Marlina`, lalu klik Tab System Log
11. Verifikasi tabel Tab System Log aktor tampil
12. Verifikasi jumlah entri Tab System Log aktor sama dengan baseline langkah 1
13. Buka Activity Log FAMS
14. Verifikasi tabel Activity Log tampil
15. Verifikasi jumlah entri Activity Log sama dengan baseline langkah 1

### TC-FA-SU-1122 (butir e, log): penolakan Assign Transaction Role tidak menulis entri log

16. Catat baseline: jumlah entri pada Tab Changelog Gita Permata, Tab Changelog Vina Maharani, Tab System Log aktor (Lina Marlina), dan Activity Log FAMS
17. Kirim permintaan langsung ke API assign Transaction Role untuk Gita Permata: Group IT Infrastructure, Transaction Transfer, Role Monitoring & Report memakai klien HTTP dengan token sesi Lina Marlina
18. Verifikasi langkah 17 ditolak server dengan status 422 dan pesan copy `V-09` "Gita Permata is no longer eligible. Please select another."
19. Kirim permintaan langsung assign Transaction Role untuk Gita Permata dengan dua grup: Accounts Payable dan IT Infrastructure (Transaction Transfer, Role Monitoring & Report) memakai klien HTTP dengan token sesi Lina Marlina
20. Verifikasi langkah 19 ditolak seluruhnya dengan status 422 dan pesan copy `V-09` "Gita Permata is no longer eligible. Please select another."
21. Kirim permintaan langsung tambah grup Branch Surabaya ke baris Disposal × Asset Admin milik Gita Permata (padanan Assign Group) memakai klien HTTP dengan token sesi Lina Marlina
22. Verifikasi langkah 21 ditolak dengan status 422 dan pesan copy `V-09` "Gita Permata is no longer eligible. Please select another."
23. Kirim permintaan langsung assign Transaction Role untuk Vina Maharani: Group Region Jawa, Transaction Transfer, Role Monitoring & Report memakai klien HTTP dengan token sesi Lina Marlina
24. Verifikasi langkah 23 ditolak dengan status 422 dan pesan copy `V-09` "Vina Maharani is no longer eligible. Please select another."
25. Tunggu 5 detik tanpa memuat ulang halaman
26. Buka Settings > User lewat sidebar, ketik Search `Gita Permata`, tekan Enter, klik Name `Gita Permata`, lalu klik Tab Changelog
27. Verifikasi tabel Tab Changelog Gita Permata tampil
28. Verifikasi jumlah entri Tab Changelog Gita Permata sama dengan baseline langkah 16
29. Buka Settings > User lewat sidebar, ketik Search `Vina Maharani`, tekan Enter, klik Name `Vina Maharani`, lalu klik Tab Changelog
30. Verifikasi tabel Tab Changelog Vina Maharani tampil
31. Verifikasi jumlah entri Tab Changelog Vina Maharani sama dengan baseline langkah 16
32. Buka Settings > User lewat sidebar, ketik Search `Lina Marlina`, tekan Enter, klik Name `Lina Marlina`, lalu klik Tab System Log
33. Verifikasi tabel Tab System Log aktor tampil
34. Verifikasi jumlah entri Tab System Log aktor sama dengan baseline langkah 16
35. Buka Activity Log FAMS
36. Verifikasi tabel Activity Log tampil
37. Verifikasi jumlah entri Activity Log sama dengan baseline langkah 16

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- S-05 dan prinsip 13g: TC-FA-SU-1116 (butir c, bagian "tidak ada entri log baru di ketiga permukaan") dan TC-FA-SU-1122 (butir e, bagian yang sama) terbelah antara asersi fungsional dan absence. Penolakan 422, pesan `V-09`, dan klausa "penugasan tidak berubah" diasersi di spec 430; spec ini memuat aksi nyata yang sama (permintaan langsung) dengan baseline sendiri per TC dan hanya mengasersi absence log. Rujukan yang sama ada di `## Notes` spec 430.
- P-5 butir a: permintaan langsung kelas a (langkah 2, 4, 17, 19, 21, 23) hanya pemicu kondisi yang diasersi tidak tercatat dan bukan objek uji. Tiap TC punya baseline sendiri (langkah 1 dan 16).
- Anchor positif (bagian 8b butir 2): pemicu yang ditolak tidak menyentuh entri yang dapat dijadikan pembanding, sehingga anchor berupa (a) `Verifikasi` penolakan server 422 dengan pesan `V-09` yang membuktikan permintaan diproses server (langkah 3, 5, 18, 20, 22, 24; tambahan terhadap Expected a dan b TC yang diasersi penuh di spec 430) dan (b) `Verifikasi` tabel tiap surface tampil sebelum jumlah entri dibandingkan dengan baseline (langkah 8, 11, 14, 27, 30, 33, 36). Pembanding jumlah awal dicatat di langkah 1 dan 16.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1 dan 16 (baseline, S-12), langkah 6 dan 25 (jendela 5 detik), serta langkah 7, 10, 13, 26, 29, 32, dan 35 (membuka surface). Search `Gita Permata`, `Vina Maharani`, dan `Lina Marlina` pada langkah 7, 10, 26, 29, dan 32 adalah langkah penghubung untuk menemukan baris target (R-16, R-23). Klik sidebar mereset Search sehingga tiap pembukaan baris target diawali Search baru.
- Langkah pola baca-log: langkah 7 sampai 15 dan langkah 26 sampai 37 (buka surface, `Verifikasi` tabel tampil, lalu `Verifikasi` jumlah entri). Blok ini tidak dihitung terhadap ambang sekitar 35 langkah. Spec ini 37 langkah nominal (16 di luar blok baca-log): semua langkah satu kelas (absence log, kelas g) dengan pemicu permintaan langsung yang sama, dan tiap TC wajib punya baseline sendiri serta `Verifikasi` per surface (S-01, S-12).
- Tab Changelog dibaca untuk tiap pengguna target (Gita Permata pada kedua TC, Vina Maharani pada TC-FA-SU-1122), sedangkan Tab System Log aktor dan Activity Log FAMS membaca log aktor Lina Marlina yang memicu permintaan. Jumlah entri dibandingkan dengan baseline (S-12); total entri tidak diasersi sebagai angka absolut.
- Temuan untuk QA:
  - Expected TC-FA-SU-1116 butir c dan TC-FA-SU-1122 butir e menyebut "ketiga permukaan" tanpa menyebut nama; spec membaca Tab Changelog target, Tab System Log aktor, dan Activity Log FAMS mengikuti Langkah Uji 3 dan 5 TC. Mohon dikonfirmasi.
  - TC-FA-SU-1122 mempunyai dua target (Gita Permata dan Vina Maharani); "Tab Changelog target" dibaca untuk keduanya karena TC tidak menyebut target yang dimaksud.
  - Tabel surface log tidak memiliki entri pembanding yang dijamin ada untuk Gita Permata dan Vina Maharani (isi log seed #51 tidak ditetapkan TC); anchor berupa penolakan 422 beserta tabel tampil dan jumlah awal yang dicatat, bukan entri pembanding spesifik.
  - NC-27: bentuk tampilan penolakan 422 `V-09` belum ditetapkan; spec tidak mengasersi tampilan (permintaan langsung).
  - Seed Pre-setup #51 (`FaUserHGT`) dan kemampuan baca jumlah entri tiga surface disediakan tim FE/BE.
