# Usulan Naik ke "Di Dalam Filter": Admin Console > License Allocation (License)

Modul: Admin Console > License Allocation > License (Allocate, Edit Allocation, Approval, Cost, Allocation Log, Download)
Sumber tabel: laporan progres e2e, scope `out` (luar filter), `AdminConsole/LicenseAllocationLicense`
Tanggal: 2026-11-13

## Kriteria

Spek dinaikkan ke "di dalam filter" bila dampak bisnisnya tinggi kalau spek itu benar-benar bug, tanpa melihat status run terakhir. Bila spek gagal karena kekurangan helper atau fitur belum dibangun, spek tetap diusulkan tapi ditandai di kolom Gap.

Semua spek di modul ini berstatus "Belum ada skrip". Penilaian sepenuhnya dari dampak bisnis.

## Daftar Usulan Naik

| Spek | Judul | Prioritas | Alasan dampak bisnis | Status run | Gap |
|---|---|---|---|---|---|
| E2E-040 | Cost Terkunci: Pembulatan Half-up, Cost Nol, dan Nominal Sama dari Preview sampai Capture | High | Nominal biaya yang salah berarti tagihan salah | Belum ada skrip | tidak |
| E2E-053 | Preview Cost Hari Terakhir Term dan Zona Waktu Plan Owner | High | Tanggal akhir atau zona waktu salah membuat biaya periode salah | Belum ada skrip | tidak |
| E2E-073 | Job Timeout Auto-Cancel vs Approve pada Batas SLA | High | Alokasi bisa tercommit dan batal bersamaan | Belum ada skrip | tidak |
| E2E-010 | Modal Allocation Log: Loading dan Immutability Entri | Medium | Entri log yang bisa berubah melanggar jejak audit | Belum ada skrip | tidak |

## Yang Tidak Dinaikkan

- E2E-031: validasi batas Additional Quantity. Validasi format dan batas, dampak sedang.
- E2E-012: Guided Tooltip. Tampilan.
- E2E-049, E2E-084: notifikasi in-app dan race notifikasi. Dampak notifikasi, bukan data.
- E2E-070: validasi field Edit Allocation. Validasi format.
- E2E-112: download di atas 5.000 baris. Volume ekspor.
- E2E-122: format cost dua desimal dan pemisah ribuan pada log. Tampilan.
- E2E-139: preservasi state list multi-konteks. Tampilan.

## Catatan untuk FE/QA

- Semua spek di modul ini belum punya hasil run. Setelah dijalankan, daftar ini perlu dicek ulang.
