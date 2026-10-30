---
id: TC-GS-TAG-E2E-062-un-retire-ditolak-kuota-penuh-atau-terlampaui
title: "Un-Retire Ditolak oleh Supply Asset saat Kuota Tipe Penuh atau Terpakai Melebihi Kuota"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-TAG-350
  - TC-GS-TAG-351
coverage:
  web: automated
---

# Un-Retire Ditolak oleh Supply Asset saat Kuota Tipe Penuh atau Terpakai Melebihi Kuota

## Prerequisites

- Mode: FE+BE (backend nyata; blokir karena kondisi data kuota, prinsip 12). Spec ini tidak menghapus data. Spec mengubah kuota RFID – Object TAG Client A (state global) dan memulihkannya di hook `after`.
- Akun aktor (dua sesi UI paralel dalam konteks browser terpisah, penanda `[Client A]` dan `[Supply Asset]`; penolakan diasersi di Supply Asset, ketiadaan pembaruan diasersi di registri Client A yang tetap terbuka):
  - Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; registri Client A dibuka pada langkah 1 dan 14 dan dibiarkan terbuka tanpa dimuat ulang selama pengamatan. Hook `after` menutup konteks Supply Asset dan mengembalikan sesi ke akun ini sebagai default suite.
  - Akun Supply Asset yang berwenang un-retire: tidak ada di Pre-setup TC; akun dan kredensial disediakan tim FE (S-13). Sesi UI dipakai karena penolakan diasersi di Supply Asset; sesi dibuka pada konteks browser kedua.
- Layar awal: hook `beforeEach` membuka Global Settings > TAG > Tab All.
- Data Pre-setup: Seed Registri A (Client A, DD-01..DD-30; kartu RFID – Object TAG `21 of 50`), dengan DD-08 `E2801160600002054D8A0008` (RFID Retired). Kuota RFID – Object TAG Client A disetel lewat fixture BE: sama dengan terpakai (21) untuk TC-GS-TAG-350, dan 20 sementara terpakai 21 (`21 of 20`) untuk TC-GS-TAG-351. Identifier tetap, tidak bisa bersufiks `{runId}` (S-12, Q-4).
- Kemampuan teknis (disediakan tim FE/BE): penyetelan kuota RFID – Object TAG Client A lewat fixture BE (21 dan 20); seed dan reset idempotent Seed Registri A dan kuota; pembacaan jumlah entri TAG Log DD-08 (baseline). Langkah dan selektor Un-retire di Supply Asset tidak didefinisikan di TC, PRD, atau LLD (Q-9).
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): pulihkan kuota RFID – Object TAG Client A ke 50, kembalikan Seed Registri A (DD-08 Retired), dan sesi ke Total Control Client A.
- Jendela propagasi antar-sesi: asersi absence di registri Client A yang terbuka didahului "Tunggu jendela propagasi event (durasi: NC-54, disediakan tim FE) tanpa memuat ulang halaman"; durasi belum ditetapkan di TC, PRD, atau LLD (NC-54, status Belum).
- Suite serial (`parallel: false`). State global yang diubah: kuota RFID – Object TAG Client A (dipulihkan hook `after`).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate`, lihat `suite.md`.

## Test Steps

### TC-GS-TAG-350: Un-retire saat kuota penuh

1. [Client A] Setel kuota RFID – Object TAG Client A menjadi 21 (sama dengan terpakai) lewat fixture BE, muat ulang halaman
2. [Client A] Verifikasi kartu RFID – Object TAG `21 of 21`
3. [Client A] Verifikasi DD-08 berstatus `Retired`
4. [Client A] Buka menu baris DD-08, klik `TAG Log`, catat jumlah entri, lalu tutup popup
5. [Supply Asset] Buka sesi UI terpisah dengan akun Supply Asset yang berwenang un-retire
6. [Supply Asset] Lakukan Un-retire pada tag DD-08 di Supply Asset
7. [Supply Asset] Verifikasi Un-retire ditolak oleh Supply Asset
8. [Client A] Tunggu jendela propagasi event (durasi: NC-54, disediakan tim FE) tanpa memuat ulang halaman
9. [Client A] Verifikasi status DD-08 tetap `Retired`
10. [Client A] Verifikasi kartu RFID – Object TAG tetap `21 of 21`
11. [Client A] Buka menu baris DD-08, lalu klik `TAG Log`
12. [Client A] Verifikasi tidak ada entri `Recovered` (jumlah entri sama dengan yang dicatat)
13. [Client A] Tutup popup TAG Log

### TC-GS-TAG-351: Un-retire saat terpakai melebihi kuota

14. [Client A] Setel kuota RFID – Object TAG Client A menjadi 20 sementara terpakai 21 lewat fixture BE, muat ulang halaman
15. [Client A] Verifikasi kartu RFID – Object TAG `21 of 20`
16. [Client A] Verifikasi DD-08 berstatus `Retired`
17. [Client A] Buka menu baris DD-08, klik `TAG Log`, catat jumlah entri, lalu tutup popup
18. [Supply Asset] Buka sesi UI terpisah dengan akun Supply Asset yang berwenang un-retire
19. [Supply Asset] Lakukan Un-retire pada tag DD-08 di Supply Asset
20. [Supply Asset] Verifikasi Un-retire ditolak oleh Supply Asset
21. [Client A] Tunggu jendela propagasi event (durasi: NC-54, disediakan tim FE) tanpa memuat ulang halaman
22. [Client A] Verifikasi status DD-08 tetap `Retired`
23. [Client A] Verifikasi kartu RFID – Object TAG tetap `21 of 20`
24. [Client A] Buka menu baris DD-08, lalu klik `TAG Log`
25. [Client A] Verifikasi tidak ada entri `Recovered` (jumlah entri sama dengan yang dicatat)
26. [Client A] Tutup popup TAG Log

## Notes

- Mode: FE+BE. Kelas data-kuota (prinsip 12) dengan dua sesi UI paralel. Subjudul `###` memetakan langkah ke id TC granular.
- Pengecualian P-2: konteks browser kedua (Supply Asset) hanya memicu Un-retire pada tag DD-08; yang diasersi di sesi registri Client A adalah ketiadaan pembaruan tanpa muat ulang (langkah 9 sampai 12 dan 22 sampai 25), dan penolakan di Supply Asset (langkah 7 dan 20).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 1 dan 14 (menyetel kuota lewat fixture BE sebagai precondition TC), 4 dan 17 (baseline jumlah entri TAG Log), 13 dan 26 (menutup popup TAG Log), 5 dan 18 (membuka sesi UI Supply Asset terpisah), 8 dan 21 (menunggu jendela propagasi event tanpa memuat ulang halaman agar asersi absence bermakna; durasi mengikuti NC-54).
- Asersi tambahan di luar Expected TC (S-03): langkah 2, 3, 15, dan 16 memverifikasi keadaan awal precondition (kuota dan status Retired) agar "tetap" bermakna; langkah 12 dan 25 memakai baseline jumlah entri (S-12) untuk Expected "tidak ada entri `Recovered`".
- Expected a ("tidak ada event ke registri") diamati lewat langkah 9, 10, dan 12 (TC-GS-TAG-350) dan langkah 22, 23, dan 25 (TC-GS-TAG-351): status, kartu, dan TAG Log DD-08 tidak berubah pada registri yang tetap terbuka.
- Temuan untuk QA:
  - Q-9: langkah, selektor, dan copy penolakan Un-retire di Supply Asset tidak didefinisikan; langkah 7 dan 20 hanya mengasersi bahwa Un-retire ditolak (tanpa teks).
  - NC-54 (status Belum): durasi jendela propagasi event pada langkah 8 dan 21 belum ditetapkan; nilai disediakan tim FE.
  - Precondition TC-GS-TAG-350 dan 351 menetapkan Total Control Client A dengan kuota RFID – Object TAG disetel lewat fixture BE; spec memakai Client A. Client Quota di Pre-setup TC berkuota GPS 3 dan NFC 0 dan tidak memuat DD-08.
  - Q-4: identifier tetap; kuota yang diubah di Client A dipulihkan di hook `after`.
  - Post Condition TC-GS-TAG-350 dan 351 tidak ada.
