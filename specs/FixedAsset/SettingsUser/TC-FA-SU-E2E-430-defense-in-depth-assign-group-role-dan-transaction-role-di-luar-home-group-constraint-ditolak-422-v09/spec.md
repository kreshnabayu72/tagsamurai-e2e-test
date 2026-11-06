---
id: TC-FA-SU-E2E-430-defense-in-depth-assign-group-role-dan-transaction-role-di-luar-home-group-constraint-ditolak-422-v09
title: "Defense-in-depth: Permintaan Langsung Assign Group Role dan Assign Transaction Role ke Node di Luar Home Group Constraint Ditolak 422 dengan Copy V-09 dan Seluruh Save Batal"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-1116
  - TC-FA-SU-1122
coverage:
  web: automated
---

# Defense-in-depth: Permintaan Langsung Assign Group Role dan Assign Transaction Role ke Node di Luar Home Group Constraint Ditolak 422 dengan Copy V-09 dan Seluruh Save Batal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook suite dan sesi API aktor dinyatakan di `suite.md`.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), dan Pre-setup #51 (`FaUserHGT`, varian `FaUserMain` dengan Home Group tidak dikosongkan). Seed #51 belum tersedia dan disediakan tim FE/BE; dipulihkan lewat seed API di hook `before`.
- Target TC-FA-SU-1116: Gita Permata (Home Group Finance & Accounting, Pre-setup #20). Grup di luar constraint: IT Infrastructure, Branch Surabaya. Grup dalam constraint: Accounts Payable. Group Role: Manage files.
- Target TC-FA-SU-1122: Gita Permata (Home Group Finance & Accounting; Disposal × Asset Admin pada Finance & Accounting) dan Vina Maharani (Home Group Jakarta Selatan Distribution Center, parent Region Jawa). Node di luar constraint: IT Infrastructure, Branch Surabaya, Region Jawa. Transaction Transfer, Role Monitoring & Report.
- Nilai nama pengguna, grup, dan penugasan dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): klien HTTP dengan token sesi API aktor (Total Control Lina Marlina) untuk permintaan langsung assign Group Role, assign Transaction Role, dan tambah grup ke baris Transaction Role; pembacaan penugasan Group Role dan Transaction Role Gita Permata dan Vina Maharani lewat API.
- State global dan pemulihan: semua permintaan diharapkan ditolak sehingga penugasan tidak berubah. Bila ada yang diterima, penugasan dipulihkan ke Pre-setup #51 lewat seed API di hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-1116: Permintaan langsung Assign Group Role ke node di luar Home Group constraint ditolak server 422 dengan copy V-09 dan seluruh Save batal

1. Baca penugasan Group Role Gita Permata lewat API sebagai pembanding
2. Kirim permintaan langsung ke API assign Group Role Manage files untuk Gita Permata dengan grup IT Infrastructure memakai klien HTTP dengan token sesi Lina Marlina
3. Verifikasi langkah 2 ditolak server dengan status 422
4. Verifikasi respons langkah 2 memuat pesan copy `V-09` "Gita Permata is no longer eligible. Please select another."
5. Kirim permintaan langsung assign Group Role Manage files untuk Gita Permata dengan dua grup: Accounts Payable dan Branch Surabaya memakai klien HTTP dengan token sesi Lina Marlina
6. Verifikasi langkah 5 ditolak seluruhnya dengan status 422
7. Verifikasi respons langkah 5 memuat pesan copy `V-09` "Gita Permata is no longer eligible. Please select another."
8. Verifikasi Accounts Payable yang berada dalam constraint tidak ikut tersimpan pada penugasan Group Role Manage files Gita Permata (dibaca lewat API)
9. Verifikasi penugasan Group Role Gita Permata tidak berubah dibanding langkah 1 (dibaca lewat API)

### TC-FA-SU-1122: Permintaan langsung Assign Transaction Role ke node di luar Home Group constraint ditolak server 422 dengan copy V-09 dan seluruh Save batal

10. Baca penugasan Transaction Role Gita Permata dan Vina Maharani lewat API sebagai pembanding
11. Kirim permintaan langsung ke API assign Transaction Role untuk Gita Permata: Group IT Infrastructure, Transaction Transfer, Role Monitoring & Report memakai klien HTTP dengan token sesi Lina Marlina
12. Verifikasi langkah 11 ditolak server dengan status 422
13. Verifikasi respons langkah 11 memuat pesan copy `V-09` "Gita Permata is no longer eligible. Please select another."
14. Kirim permintaan langsung assign Transaction Role untuk Gita Permata dengan dua grup: Accounts Payable dan IT Infrastructure (Transaction Transfer, Role Monitoring & Report) memakai klien HTTP dengan token sesi Lina Marlina
15. Verifikasi langkah 14 ditolak seluruhnya dengan status 422
16. Verifikasi respons langkah 14 memuat pesan copy `V-09` "Gita Permata is no longer eligible. Please select another."
17. Verifikasi Accounts Payable yang berada dalam constraint tidak ikut tersimpan pada penugasan Transaction Role Gita Permata (dibaca lewat API)
18. Kirim permintaan langsung tambah grup Branch Surabaya ke baris Disposal × Asset Admin milik Gita Permata (padanan Assign Group) memakai klien HTTP dengan token sesi Lina Marlina
19. Verifikasi langkah 18 ditolak dengan status 422
20. Verifikasi respons langkah 18 memuat pesan copy `V-09` "Gita Permata is no longer eligible. Please select another."
21. Verifikasi baris Disposal × Asset Admin Gita Permata tetap memuat Finance & Accounting saja (dibaca lewat API)
22. Kirim permintaan langsung assign Transaction Role untuk Vina Maharani: Group Region Jawa, Transaction Transfer, Role Monitoring & Report memakai klien HTTP dengan token sesi Lina Marlina
23. Verifikasi langkah 22 ditolak dengan status 422: gate mengevaluasi node penugasan Region Jawa sehingga ancestor ditolak walau cakupannya mencakup node constraint Jakarta Selatan Distribution Center
24. Verifikasi respons langkah 22 memuat pesan copy `V-09` "Vina Maharani is no longer eligible. Please select another."
25. Verifikasi penugasan Transaction Role Gita Permata tidak berubah dibanding langkah 10 (dibaca lewat API)
26. Verifikasi penugasan Transaction Role Vina Maharani tidak berubah dibanding langkah 10 (dibaca lewat API)

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- K-1 dan bagian 8b butir 1: TC-FA-SU-1116 dan TC-FA-SU-1122 bertipe Security dengan kolom FE Test kosong (`-`) dan Expected berupa respons API (status respons dan state data). Kedua TC tetap masuk spec FE+BE walau tumpang tindih dengan pengujian tingkat endpoint, mengikuti spec 335 dan 422. Asersi spec hanya status respons, isi pesan respons, dan state data (dibaca lewat API); tampilan UI (toast atau inline) tidak diasersi.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, S-03): langkah 1 dan 10 membaca penugasan sebagai pembanding bagi asersi "tidak berubah"; langkah 2, 5, 11, 14, 18, dan 22 adalah pemicu (permintaan langsung), bukan asersi.
- S-05: Expected butir c TC-FA-SU-1116 ("tidak ada entri log baru di ketiga permukaan") dan butir e TC-FA-SU-1122 ("tidak ada entri log baru di ketiga permukaan") adalah asersi absence dan diasersi di spec 431 dengan permintaan langsung yang sama sebagai pemicu, baseline sendiri, dan anchor positif. Spec ini tidak mengasersi log; klausa "penugasan tidak berubah" kedua TC diasersi di langkah 9, 25, dan 26.
- Tiap permintaan ditolak dengan pesan copy `V-09` (`[User Name]` diganti nama pengguna target): langkah 4, 7, 13, 16, 20 memakai "Gita Permata is no longer eligible. Please select another." dan langkah 24 memakai "Vina Maharani is no longer eligible. Please select another.".
- Temuan untuk QA:
  - TC-FA-SU-1116 dan TC-FA-SU-1122 bertipe Security dengan kolom FE Test kosong namun tidak tercatat hanya-BE; spec ditulis FE+BE dengan klien HTTP bertoken sesi aktor mengikuti spec 335 dan 422. Mohon dikonfirmasi bila seharusnya dicatat hanya-BE.
  - NC-27: bentuk tampilan penolakan 422 `V-09` (toast atau inline) belum ditetapkan. Kedua TC menyebut "tanpa tampilan toast" untuk permintaan langsung; spec tidak mengasersi bentuk tampilan apa pun (bagian 8b butir 1).
  - Copy `V-09` memuat `[User Name]`; spec mengasumsikan nilainya nama pengguna target (asumsi sinkron TC). TC-FA-SU-1122 butir d memakai Vina Maharani. Mohon dikonfirmasi.
  - TC menyebut "API assign Group Role", "API assign Transaction Role", dan "tambah grup ke baris" tanpa nama atau jalur endpoint; spec tidak menulis jalur endpoint (S-13), dan klien HTTP beserta jalur yang dipakai disediakan tim FE/BE.
  - TC-FA-SU-1116 butir b mengasersi grup dalam constraint (Accounts Payable) tidak ikut tersimpan. Perilaku Save pada popup Assign Group Role bila baris Group Role lama berada di luar constraint tidak ditetapkan PRD dan tidak diasersi.
  - Seed Pre-setup #51 (`FaUserHGT`) dan kunci fixture untuk node Accounts Payable, Region Jawa, Jakarta Selatan Distribution Center, dan penugasan #51 disediakan tim FE/BE sebelum eksekusi.
