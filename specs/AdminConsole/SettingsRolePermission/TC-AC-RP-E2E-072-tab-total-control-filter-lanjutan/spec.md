---
id: TC-AC-RP-E2E-072-tab-total-control-filter-lanjutan
title: "Filter Tab Total Control: Modified By, Last Updated, multi-field, kolom curated"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-240
  - TC-AC-RP-241
  - TC-AC-RP-242
  - TC-AC-RP-243
coverage:
  web: automated
---

# Filter Tab Total Control: Modified By, Last Updated, multi-field, kolom curated

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD` (nama env baru, perlu didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip halaman ini: mengikuti pernyataan hook suite di `suite.md`.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Nilai data (nama user, group, role, kolom) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script).
- Data Pre-setup Tab Total Control (Pre-setup #1 dan #13), enam baris urutan Name A-Z: `Bambang Hartono` (CEO, Board; Modified By dan Last Updated "—"), `Budi Santoso` (Supervisor, Warehouse, Pending Activation; "Siti N" 08 Jun 2026, 09:30), `John Doe` (Manager, Finance; "Siti N" 15 Jun 2026, 10:05), `Rina Wijaya` (Staff, Finance; "Bambang H" 05 Jun 2026, 15:20), `Sarah Kim` (Staff, Operations, Inactive; "John D" 10 Jun 2026, 14:50), `Siti Nurhaliza` (Admin Lead, IT; "Bambang H" 01 Jun 2026, 08:00).
- Data yang diubah: user Standard `Agus Salim` (Pre-setup #12; akun sementara sampai 31 Des 2026, TAG `TAG-0001`) di-assign Total Control oleh spec ini (Tabel Data Uji Dinamis #3). Data Pre-setup bersama ini tidak dapat dimiliki spec; pemulihannya (kembali Standard) dijamin kemampuan reset baseline yang disediakan tim FE/BE (hook `before` dan `after`, sesuai `suite.md`). Efek: baris `Agus Salim` memperoleh Modified By `Siti N` dan Last Updated waktu aksi; entri Changelog dan System Log bertambah (audit trail tidak dihapus). Tidak ada record bersuffix `+{runId}-NNN` yang dibuat.
- Data Pre-setup `Agus Salim` (Standard, akun sementara) eligible di pool picker Assign Total Control dan belum memegang tingkat akses pada awal spec (kondisi baseline); TC-AC-RP-243 dijalankan terakhir agar TC lain memakai enam baris awal.
- Pemulihan Setup Column: preferensi kolom di browser dihapus di hook `after` (kemampuan disediakan tim FE; bukan `[Reset to Default]`).
- Kemampuan teknis: kemampuan reset baseline (tim FE/BE) dan penghapusan preferensi kolom di browser (tim FE).

## Test Steps

### TC-AC-RP-240: Filter Tab Total Control berdasarkan Modified By

1. Klik ikon Filter
2. Buka dropdown Modified By
3. Verifikasi opsi dropdown Modified By berasal dari nilai unik kolom Modified By pada data tabel
4. Ketik `Siti` pada kotak pencarian dropdown Modified By
5. Verifikasi opsi "Siti N" tampil pada hasil pencarian dropdown Modified By (dropdown dapat dicari)
6. Pilih Modified By "Siti N"
7. Klik `[Apply]`
8. Verifikasi baris `John Doe` dan `Budi Santoso` tampil
9. Verifikasi seluruh baris yang tampil ber-Modified By "Siti N"

### TC-AC-RP-241: Filter Last Updated date range dan baris tanpa nilai

10. Klik `[Clear Field]`, lalu klik `[Apply]`
11. Pilih Last Updated 08 Jun 2026 sampai 15 Jun 2026
12. Klik `[Apply]`
13. Verifikasi baris `John Doe`, `Sarah Kim`, dan `Budi Santoso` (Last Updated dalam rentang) tampil
14. Verifikasi baris `Bambang Hartono` (Last Updated "—") tidak tampil

### TC-AC-RP-242: Filter multi-field dan Clear Field

15. Klik `[Clear Field]`, lalu klik `[Apply]`
16. Pilih Division `Finance`
17. Pilih Status `Active`
18. Klik `[Apply]`
19. Verifikasi baris `John Doe` dan `Rina Wijaya` tampil
20. Verifikasi tidak ada baris selain `John Doe` dan `Rina Wijaya` (hanya baris yang memenuhi kedua kondisi)
21. Klik `[Clear Field]`
22. Klik `[Apply]`
23. Verifikasi seluruh 6 baris tampil (`Bambang Hartono`, `Budi Santoso`, `John Doe`, `Rina Wijaya`, `Sarah Kim`, `Siti Nurhaliza`)

### TC-AC-RP-243: Filter Temporary User dan Temporary Until setelah kolom curated ditampilkan

24. Klik tombol "+ Assign"
25. Centang `Agus Salim`
26. Klik `[Assign]`
27. Verifikasi toast "Success, Total Control has been assigned."
28. Verifikasi baris `Agus Salim` tampil
29. Tampilkan kolom Temporary User dan Temporary Until lewat Column Visibility
30. Verifikasi kolom Temporary Until baris non-sementara (mis. `John Doe`) tampil "—"
31. Pilih Temporary User `Yes` pada Filter Panel
32. Klik `[Apply]`
33. Verifikasi baris `Agus Salim` (akun sementara) tampil
34. Verifikasi tidak ada baris selain akun sementara

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Spec fungsional tanpa kelas harness khusus.
- Langkah penghubung (tanpa awalan Verifikasi): langkah 10 dan 15 (`[Clear Field]` lalu `[Apply]`) mengosongkan filter sebelum TC berikutnya (S-09); Filter Panel dibuka sekali di langkah 1.
- Penyimpangan urutan di TC-AC-RP-243: Verifikasi kolom Temporary Until baris non-sementara "—" (langkah 30) ditulis sebelum filter Temporary User `Yes`, karena sesudah filter hanya akun sementara yang tampil sehingga baris non-sementara tidak dapat diamati.
- Verifikasi toast dan baris `Agus Salim` setelah Assign berasal dari tanda "→ toast sukses dan baris `Agus Salim` tampil" pada langkah TC-AC-RP-243 (S-03); teks toast diambil dari TC-AC-RP-122.
- Langkah mengetik pada kotak pencarian dropdown menjabarkan klausa "dapat dicari" pada Expected TC-AC-RP-240 (S-03).
- Temuan untuk QA:
  - TC-AC-RP-243 Expected memuat kolom Temporary Until baris non-sementara "—" bersama hasil filter Temporary User `Yes`; keduanya tidak dapat diamati bersamaan (baris non-sementara tersaring); spec mengasersi "—" sebelum filter.
  - TC-AC-RP-243 tidak menyebut teks toast Assign; teks diambil dari TC-AC-RP-122.
  - TC tidak menyatakan apakah Filter Panel tetap terbuka setelah `[Apply]` (TC-AC-RP-242 memakai `[Clear Field]` tanpa membuka ulang); Column Visibility tidak menyebut `[Save]`.
