# Usulan Naik ke "Di Dalam Filter": Admin Console > Device Allocation

Modul: Admin Console > Device Allocation (Allocate, Resubmit, Approval, Log, Konfigurasi, Multi-konteks)
Sumber tabel: laporan progres e2e, scope `out` (luar filter), `AdminConsole/DeviceAllocation`
Tanggal: 2026-11-13

## Kriteria

Spek dinaikkan ke "di dalam filter" bila dampak bisnisnya tinggi kalau spek itu benar-benar bug, tanpa melihat status run terakhir. Bila spek gagal karena kekurangan helper atau fitur belum dibangun, spek tetap diusulkan tapi ditandai di kolom Gap.

Semua spek di modul ini berstatus "Belum ada skrip". Penilaian sepenuhnya dari dampak bisnis.

## Daftar Usulan Naik

| Spek | Judul | Prioritas | Alasan dampak bisnis | Status run | Gap |
|---|---|---|---|---|---|
| E2E-023 | Submit Allocate Device: Double-Submit Hanya Memproses Satu Request dan Penolakan Server saat Saldo Berubah | High | Double-submit bisa memotong saldo dua kali | Belum ada skrip | tidak |
| E2E-032 | Resubmit Diblokir Kondisi Data: Validasi Quantity, Saldo Kurang, Client Tidak Valid, Kantong Sumber Tidak Tersedia | High | Alokasi bisa lolos saat saldo atau client tidak valid | Belum ada skrip | tidak |
| E2E-048 | Integritas Log: Satu Entri per Aksi, Entri Lama Immutable, Aksi Gagal Tidak Mengubah Log | High | Jejak alokasi harus tepat dan tidak berubah | Belum ada skrip | tidak |
| E2E-053 | Konfigurasi dan Data Master: Dibaca Live atau Snapshot (Harga, Nama Client, Pengirim, Paid From, Allocated By, Approval) | High | Harga atau aturan approval yang dibaca salah bisa menyebabkan salah bayar atau salah approve | Belum ada skrip | tidak |
| E2E-056 | Multi-Konteks: Konflik Dua Approver, Review Basi Setelah Cancel atau Edit, Edit Bersamaan | High | Dua approver bisa menyetujui atau menimpa hasil yang sama | Belum ada skrip | tidak |
| E2E-057 | Race Commit Timeout Auto-Cancel Melawan Cancel Manual dan Approve | High | Alokasi bisa tercommit dan batal bersamaan | Belum ada skrip | tidak |
| E2E-061 | Plan Gating: Modul Device Allocation Berperilaku Sama pada Plan Terendah dan Tertinggi | Medium | Plan gating yang salah bisa membuka atau menutup fitur | Belum ada skrip | tidak |

## Yang Tidak Dinaikkan

- E2E-045: download di atas 5.000 baris. Dampaknya ke volume ekspor, bukan kebenaran alokasi.

## Catatan untuk FE/QA

- Semua spek di modul ini belum punya hasil run. Setelah dijalankan, daftar ini perlu dicek ulang.
