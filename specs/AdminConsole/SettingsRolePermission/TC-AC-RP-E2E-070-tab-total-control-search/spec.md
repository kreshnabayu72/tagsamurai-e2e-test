---
id: TC-AC-RP-E2E-070-tab-total-control-search
title: "Search Tab Total Control: kolom Searchable, Hidden, curated, Last Updated"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-233
  - TC-AC-RP-234
  - TC-AC-RP-235
coverage:
  web: automated
---

# Search Tab Total Control: kolom Searchable, Hidden, curated, Last Updated

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD` (nama env baru, perlu didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip halaman ini: mengikuti pernyataan hook suite di `suite.md`.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Nilai data (nama user, group, role, kolom) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script).
- Data Pre-setup Tab Total Control (Pre-setup #1 dan #13), enam baris urutan Name A-Z: `Bambang Hartono` (CEO, Board; Modified By dan Last Updated "—"), `Budi Santoso` (Supervisor, Warehouse, Pending Activation; "Siti N" 08 Jun 2026, 09:30), `John Doe` (Manager, Finance; "Siti N" 15 Jun 2026, 10:05), `Rina Wijaya` (Staff, Finance; "Bambang H" 05 Jun 2026, 15:20), `Sarah Kim` (Staff, Operations, Inactive; "John D" 10 Jun 2026, 14:50), `Siti Nurhaliza` (Admin Lead, IT; "Bambang H" 01 Jun 2026, 08:00).
- Data yang diubah: user Standard `Agus Salim` (Pre-setup #12; akun sementara sampai 31 Des 2026, TAG `TAG-0001`) di-assign Total Control oleh spec ini (Tabel Data Uji Dinamis #3). Data Pre-setup bersama ini tidak dapat dimiliki spec; pemulihannya (kembali Standard) dijamin kemampuan reset baseline yang disediakan tim FE/BE (hook `before` dan `after`, sesuai `suite.md`). Efek: baris `Agus Salim` memperoleh Modified By `Siti N` dan Last Updated waktu aksi; entri Changelog dan System Log bertambah (audit trail tidak dihapus). Tidak ada record bersuffix `+{runId}-NNN` yang dibuat.
- Data Pre-setup `Agus Salim` (Standard, TAG `TAG-0001`) eligible di pool picker Assign Total Control dan belum memegang tingkat akses pada awal spec (kondisi baseline).
- Pemulihan Setup Column: preferensi kolom di browser dihapus di hook `after` (kemampuan disediakan tim FE; bukan `[Reset to Default]`).
- Kemampuan teknis: kemampuan reset baseline (tim FE/BE) dan penghapusan preferensi kolom di browser (tim FE).

## Test Steps

### TC-AC-RP-233: Search Tab Total Control mencakup kolom Searchable yang visible

1. Ketik Search `finance`, tekan Enter
2. Verifikasi baris `John Doe` dan `Rina Wijaya` (Division Finance) tampil
3. Ganti isi kotak search dengan `siti n`, tekan Enter
4. Verifikasi baris dengan Name `Siti Nurhaliza` tampil
5. Verifikasi baris dengan Modified By "Siti N" (`John Doe`, `Budi Santoso`) tampil
6. Ganti isi kotak search dengan `inactive` tanpa menekan Enter
7. Verifikasi baris `Siti Nurhaliza` masih tampil
8. Verifikasi baris `Sarah Kim` belum tampil (Search belum berjalan sebelum Enter, tanpa debounce)
9. Tekan Enter pada kotak Search
10. Verifikasi baris `Sarah Kim` (Status Inactive) tampil
11. Verifikasi pencarian tidak case-sensitive (kata kunci huruf kecil `finance`, `siti n`, dan `inactive` menemukan nilai berhuruf kapital)

### TC-AC-RP-235: Search tidak mencakup kolom Last Updated

12. Klik `(←)` pada kotak Search
13. Ketik Search `15 Jun 2026`, tekan Enter
14. Verifikasi hasil "No results found" tampil (kolom Last Updated tidak Searchable)

### TC-AC-RP-234: Search tidak mencakup kolom Hidden dan mencakup kolom curated setelah ditampilkan

15. Klik `(←)` pada kotak Search
16. Klik tombol "+ Assign"
17. Centang `Agus Salim`
18. Klik `[Assign]`
19. Verifikasi toast "Success, Total Control has been assigned."
20. Verifikasi baris `Agus Salim` tampil
21. Ketik Search `tag-0001`, tekan Enter
22. Verifikasi hasil "No results found" tampil (kolom TAG Hidden tidak tercakup Search)
23. Tampilkan kolom TAG lewat Column Visibility
24. Ganti isi kotak search dengan `tag-0001`, tekan Enter
25. Verifikasi baris `Agus Salim` (TAG `TAG-0001`) tampil

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Spec fungsional tanpa kelas harness khusus.
- Langkah penghubung (tanpa awalan Verifikasi): langkah 12 dan 15 mengosongkan kotak Search (S-09); langkah 6 dan 9 memisahkan mengetik dari menekan Enter agar "baru berjalan setelah Enter (tanpa debounce)" dapat diamati; langkah 23 menampilkan kolom TAG sesuai TC.
- Penyimpangan urutan: TC-AC-RP-235 dijalankan sebelum TC-AC-RP-234 karena TC-AC-RP-234 meng-assign `Agus Salim` dan mengubah isi Tab Total Control; dua TC lain mengandalkan enam baris awal.
- Verifikasi toast (langkah 19) dan baris `Agus Salim` sesudahnya berasal dari tanda "→ toast sukses dan baris `Agus Salim` tampil" pada langkah TC-AC-RP-234 (S-03); teks toast diambil dari TC-AC-RP-122.
- Temuan untuk QA:
  - TC-AC-RP-234 hanya menyebut "toast sukses" tanpa teks; teks "Success, Total Control has been assigned." dipakai dari TC-AC-RP-122 (Assign Total Control).
  - TC-AC-RP-233 Expected c menyebut "baru berjalan setelah Enter (tanpa debounce)" tanpa langkah pengamatan di kolom Langkah Uji; langkah 6 sampai 9 ditambahkan untuk mengamatinya.
  - Column Visibility pada TC-AC-RP-234 tidak menyebut apakah perubahan perlu `[Save]`; spec mengikuti TC.
  - Assign `Agus Salim` mengubah data Pre-setup bersama; pemulihan bergantung pada kemampuan reset baseline yang tidak didefinisikan di TC, PRD, atau LLD (kemampuan disediakan tim FE/BE).
