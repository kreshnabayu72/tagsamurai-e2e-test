---
id: TC-AC-RP-E2E-074-tab-total-control-sort-kolom-lanjutan
title: "Sort Tab Total Control: Modified By, Last Updated, kolom curated"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-248
  - TC-AC-RP-249
  - TC-AC-RP-250
coverage:
  web: automated
---

# Sort Tab Total Control: Modified By, Last Updated, kolom curated

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD` (nama env baru, perlu didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip halaman ini: mengikuti pernyataan hook suite di `suite.md`.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Nilai data (nama user, group, role, kolom) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script).
- Data Pre-setup Tab Total Control (Pre-setup #1 dan #13), enam baris urutan Name A-Z: `Bambang Hartono` (CEO, Board; Modified By dan Last Updated "—"), `Budi Santoso` (Supervisor, Warehouse, Pending Activation; "Siti N" 08 Jun 2026, 09:30), `John Doe` (Manager, Finance; "Siti N" 15 Jun 2026, 10:05), `Rina Wijaya` (Staff, Finance; "Bambang H" 05 Jun 2026, 15:20), `Sarah Kim` (Staff, Operations, Inactive; "John D" 10 Jun 2026, 14:50), `Siti Nurhaliza` (Admin Lead, IT; "Bambang H" 01 Jun 2026, 08:00).
- Data yang diubah: user Standard `Agus Salim` (Pre-setup #12; akun sementara sampai 31 Des 2026, TAG `TAG-0001`) di-assign Total Control oleh spec ini (Tabel Data Uji Dinamis #3). Data Pre-setup bersama ini tidak dapat dimiliki spec; pemulihannya (kembali Standard) dijamin kemampuan reset baseline yang disediakan tim FE/BE (hook `before` dan `after`, sesuai `suite.md`). Efek: baris `Agus Salim` memperoleh Modified By `Siti N` dan Last Updated waktu aksi; entri Changelog dan System Log bertambah (audit trail tidak dihapus). Tidak ada record bersuffix `+{runId}-NNN` yang dibuat.
- Data Pre-setup `Agus Salim` (Standard, akun sementara) eligible di pool picker Assign Total Control dan belum memegang tingkat akses pada awal spec (kondisi baseline); TC-AC-RP-250 dijalankan terakhir.
- Pemulihan Setup Column: preferensi kolom di browser dihapus di hook `after` (kemampuan disediakan tim FE; bukan `[Reset to Default]`).
- Kemampuan teknis: kemampuan reset baseline (tim FE/BE) dan penghapusan preferensi kolom di browser (tim FE).

## Test Steps

### TC-AC-RP-248: Sort Tab Total Control kolom Modified By

1. Klik header kolom Modified By sekali
2. Verifikasi urutan Modified By A-Z
3. Verifikasi nilai "—" (`Bambang Hartono`) berada di akhir pada urutan A-Z
4. Klik header Modified By kedua kali
5. Verifikasi urutan Modified By Z-A
6. Verifikasi nilai "—" (`Bambang Hartono`) berada di awal pada urutan Z-A
7. Klik header Modified By ketiga kali
8. Verifikasi urutan kembali ke bawaan Name A-Z

### TC-AC-RP-249: Sort Tab Total Control kolom Last Updated

9. Klik header kolom Last Updated sekali
10. Verifikasi urutan Last Updated Oldest First
11. Verifikasi nilai "—" berada di akhir pada Oldest First
12. Klik header Last Updated kedua kali
13. Verifikasi urutan Last Updated Newest First
14. Verifikasi nilai "—" berada di awal pada Newest First
15. Klik header Last Updated ketiga kali
16. Verifikasi urutan kembali ke bawaan Name A-Z

### TC-AC-RP-250: Sort kolom curated Temporary User menempatkan No sebelum Yes

17. Klik tombol "+ Assign"
18. Centang `Agus Salim`
19. Klik `[Assign]`
20. Verifikasi toast "Success, Total Control has been assigned."
21. Verifikasi baris `Agus Salim` tampil
22. Tampilkan kolom Temporary User lewat Column Visibility
23. Klik header kolom Temporary User sekali
24. Verifikasi baris bernilai `No` (mis. `John Doe`) berada sebelum baris `Yes` (`Agus Salim`)

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Spec fungsional tanpa kelas harness khusus.
- Klik ketiga pada TC-AC-RP-248 dan TC-AC-RP-249 mengembalikan urutan bawaan sehingga TC berikutnya mulai dari keadaan netral (S-09).
- Langkah 22 menampilkan kolom Temporary User sesuai TC-AC-RP-250 (langkah penghubung, S-03).
- Verifikasi toast dan baris `Agus Salim` setelah Assign berasal dari tanda "→ toast sukses dan baris `Agus Salim` tampil" pada langkah TC-AC-RP-250 (S-03); teks toast diambil dari TC-AC-RP-122.
- Temuan untuk QA:
  - TC-AC-RP-250 tidak menyebut teks toast Assign; teks diambil dari TC-AC-RP-122.
  - Column Visibility pada TC-AC-RP-250 tidak menyebut `[Save]`; spec mengikuti TC.
