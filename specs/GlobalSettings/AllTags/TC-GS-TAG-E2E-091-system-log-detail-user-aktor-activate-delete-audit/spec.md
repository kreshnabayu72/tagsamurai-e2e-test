---
id: TC-GS-TAG-E2E-091-system-log-detail-user-aktor-activate-delete-audit
title: "System Log Detail User Aktor: Entri Activate TAG, Delete TAG, Audit TAG, dan Update TAG Condition Identik dengan Activity Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-343
  - TC-GS-TAG-344
  - TC-GS-TAG-345
coverage:
  web: automated
---

# System Log Detail User Aktor: Entri Activate TAG, Delete TAG, Audit TAG, dan Update TAG Condition Identik dengan Activity Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor utama: Total Control Client A Sari Dewi `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup TC); kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before` (akun default suite). Aktor yang diamati System Log-nya adalah akun yang sedang login.
- Akun kedua (langkah 21 sampai 23, TC-345): Total Control Client Audit Joko Santoso `totalControl_automated_qaAudit@qwertysystem.net`; kredensial `Spectra.env.GS_TC_AUDIT_PASSWORD` (belum terdaftar di `.env.example` dan `spectra.config.ts`; perlu didaftarkan pemilik repositori, tanpa nilai). Hook `after` mengembalikan sesi ke akun default suite (Client A).
- Flag Guided Tooltip `gs-tag-registry` dan `gs-tag-activate` untuk kedua akun mengikuti hook suite `before` dan `after` (lihat `suite.md`, bagian Hook Guided Tooltip).
- Suite serial (`parallel: false`). Hook `beforeEach`: buka Global Settings > TAG, Tab All.
- Hook `after` suite memulihkan Seed Registri A, Seed Client Audit, dan stok resmi secara idempotent (pernyataan hook di `suite.md`).
- Data Pre-setup (dipulihkan ke kondisi awal oleh hook `before` lewat fixture BE; mekanisme disediakan tim FE/BE, lihat Temuan untuk QA):
  - Client A: stok resmi GPS `356938035643001` (DD-S1, Available; Template Self-Purchased kosong) dan Seed Registri A (DD-02 `E2801160600002054D8A0002`, RFID Object, Available).
  - Client Audit: Seed Client Audit AU1 `E2801160600002054D8A5001` (Available, combined dengan NFC `04A224B2C15E95` Available), AU2 `...5002` (Damaged/Missing), AU3 `...5003` (Retired), AU4 `...5004` (Available).
- Kemampuan teknis (disediakan tim FE): simulasi pemindai RFID (pindai kode, `Stop` pada Floating Status Widget sebelum menyentuh kontrol halaman lain; page-lock sesi scan, NC-43; label TC `Manual Only — (b)` pada TC-345 bukan alasan mengeluarkan TC, keputusan D-4, Q-1); entri manual GPS (input lalu klik `Add`; label dan placeholder menunggu desain, NC-11); pembaca total entri pada footer; akses ke Detail User aktor > Tab System Log (modul User; selektor disediakan tim FE).
- Baseline log: Activity Log dan System Log aktor menumpuk antar spec (tidak dibersihkan), sehingga semua asersi entri baru memakai selisih total terhadap baseline yang dicatat sebelum aksi (S-12). Hanya satu aksi yang berjalan pada suite serial selama blok.
- Tabel "Entri baru sesi Audit TC-345" (parameter langkah 31 sampai 34; tag yang berubah status mengikuti aturan TC-265: AU2 `Damaged/Missing` ke `Available`; AU1 dan sibling NFC `Available` ke `Damaged/Missing`; AU3 Retired dan AU4 yang terpindai tidak berubah):

| Action | Name |
|---|---|
| `Audit TAG` | `RFID` |
| `Update TAG Condition` | `E2801160600002054D8A5002` |
| `Update TAG Condition` | `E2801160600002054D8A5001` |
| `Update TAG Condition` | `04A224B2C15E95` |

- State global yang diubah: tidak ada selain data (Seed Registri A, Seed Client Audit, dan log).

## Test Steps

### TC-GS-TAG-343: Activate TAG menulis System Log pada Detail User aktor, identik dengan Activity Log

1. Buka Detail User aktor (Sari Dewi) > Tab System Log, catat total entri `S0` pada footer
2. Buka Global Settings > Activity Log, tab User Action, catat total entri `A0` pada footer
3. Buka Global Settings > TAG, Tab All, klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, lalu klik `Continue` pada popup `Ready to Activate a TAG`
4. Tambahkan lewat entri manual `356938035643001`
5. Klik `Submit` lalu konfirmasi
6. Tunggu aksi selesai
7. Buka Global Settings > Activity Log, tab User Action
8. Verifikasi total entri menjadi `A0 + 1` dan entri teratas Action `Activate TAG` (catat Object, Name, Field, Old Value, dan New Value entri itu)
9. Buka Detail User aktor > Tab System Log
10. Verifikasi total entri menjadi `S0 + 1`
11. Verifikasi entri teratas Tab System Log memuat Action `Activate TAG`, Object `TAG Registry`, Name, Field `Status`, Old Value, dan New Value sama dengan entri Activity Log yang dicatat pada langkah 8
12. Verifikasi Tab System Log tidak memuat kolom Modified By
13. Verifikasi Old Value dan New Value entri teratas tampil sebagai plain text

### TC-GS-TAG-344: Delete TAG menulis System Log pada Detail User aktor, identik dengan Activity Log

14. Catat baseline sebelum aksi: total entri System Log aktor `S1` (Detail User aktor > Tab System Log) dan total entri Activity Log tab User Action `A1`
15. Buka Global Settings > TAG, Tab All, ketik Search `E2801160600002054D8A0002`, tekan Enter, buka menu baris DD-02, klik `Delete`, lalu konfirmasi dengan klik `Delete` pada dialog
16. Tunggu aksi selesai, lalu buka Global Settings > Activity Log, tab User Action
17. Verifikasi total entri menjadi `A1 + 1` dan entri teratas Action `Delete TAG`, Object `TAG Registry`, Name `E2801160600002054D8A0002`, Field `Status`, Old Value `Available`, New Value `Deleted (Actions)`
18. Buka Detail User aktor > Tab System Log
19. Verifikasi total entri menjadi `S1 + 1`
20. Verifikasi entri teratas Tab System Log memuat Action `Delete TAG`, Object `TAG Registry`, Name `E2801160600002054D8A0002`, Field `Status`, Old Value `Available`, New Value `Deleted (Actions)`, sama dengan entri Activity Log pada langkah 17

### TC-GS-TAG-345: Audit TAG menulis System Log aktor, satu entri Audit TAG dan satu entri Update TAG Condition per tag

21. Klik avatar akun, pilih `Logout`
22. Login sebagai Total Control Client Audit Joko Santoso (`Spectra.env.GS_TC_AUDIT_PASSWORD`)
23. Catat baseline sebelum aksi: total entri System Log aktor `S2` (Detail User aktor > Tab System Log) dan total entri Activity Log tab User Action `A2`
24. Buka Global Settings > TAG, klik Tab Not Paired, klik `Audit TAG`, lalu pilih `RFID` pada overlay `Select TAG Type`
25. Pindai AU2 dan AU4 (`E2801160600002054D8A5002` dan `E2801160600002054D8A5004`), lalu klik `Stop` pada Floating Status Widget
26. Klik `Submit`, biarkan checkbox `Mark all as Damaged/Missing` dicentang, klik `Confirm`
27. Tunggu aksi selesai, lalu buka Global Settings > Activity Log, tab User Action
28. Verifikasi total entri menjadi `A2 + 4` (satu `Audit TAG` dan tiga `Update TAG Condition`)
29. Buka Detail User aktor > Tab System Log
30. Verifikasi total entri menjadi `S2 + 4`
31. Untuk setiap baris tabel "Entri baru sesi Audit TC-345", lakukan langkah 32 sampai 34
32. Di Activity Log tab User Action, ketik Search Name, tekan Enter, lalu catat Object, Field, Old Value, dan New Value entri teratas dengan Action tersebut
33. Di Detail User aktor > Tab System Log, ketik Search Name, tekan Enter
34. Verifikasi entri teratas dengan Action tersebut memuat Object, Name, Field, Old Value, dan New Value sama dengan entri Activity Log yang dicatat pada langkah 32

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC dalam spec sama dengan sumber (343, 344, 345). TC-344 menghapus DD-02 (aksi destruktif) setelah TC-343 yang tidak membutuhkan DD-02; TC-345 di akhir karena butuh ganti akun eksplisit (langkah 21 sampai 22) dan scan; bagian itu tetap bermakna bila bagian sebelumnya gagal.
- Penyimpangan kelas: plan menandai spec ini tanpa kelas harness, tetapi TC-345 membutuhkan simulasi pemindai (kelas d, label TC `Manual Only — (b)`). Blok itu dipertahankan di akhir spec ini sesuai plan dan keputusan D-4; pemisahan ke spec kelas d dapat dipertimbangkan reviewer.
- Alasan spec di atas sekitar 35 langkah (34 langkah tertulis, sekitar 43 setelah ekspansi tabel): tiga TC mengasersi hal yang sama (entri System Log aktor identik dengan Activity Log) untuk tiga aksi dengan surface yang sama; langkah berulang per entri memakai parameter di tabel Prerequisites (bagian 8b butir 7). Langkah yang diulang: 32 sampai 34 (empat iterasi).
- Langkah penghubung (tanpa `Verifikasi`, tidak ada di TC): langkah 1, 2, 14, 23 (baseline sebelum aksi pemicu, S-12), langkah 6 dan 16 dan 27 (Tunggu aksi selesai), langkah 7, 9, 18, 29 (pindah surface), langkah 15 (mencari baris DD-02), langkah 21 sampai 22 (ganti akun), langkah 25 (`Stop` pada Floating Status Widget).
- Perbandingan "sama dengan entri Activity Log" (langkah 11, 20, 34) memakai nilai kolom yang dicatat dari entri Activity Log, sesuai Expected TC ("sama dengan entri Activity Log"), tanpa menambah nilai literal.
- Temuan untuk QA:
  - TC-345 tidak menyebut tag mana yang berubah status; jumlah `A2 + 4` dan daftar tag pada tabel Prerequisites diturunkan dari aturan TC-265 (sibling NFC mengikuti AU1; AU3 Retired dan AU4 terpindai tidak berubah). TC perlu menyebut daftar entri yang diharapkan.
  - TC-343 langkah 6 ("catat entri `Activate TAG`") tidak menyebut nilai Name dan New Value; spec membandingkan dengan entri Activity Log yang dicatat.
  - Cara membuka Detail User aktor > Tab System Log (modul User) dan selektornya tidak didefinisikan di TC (Q-9); disediakan tim FE.
  - TC-343 sampai TC-345 tidak menyebut bahwa Activity Log tab User Action adalah tab yang memuat entri ini; spec mengikuti pola ActivityLog (entri aksi pengguna di tab User Action).
  - Seeding dan reset Seed Registri A dan Seed Client Audit antar spec tidak didefinisikan di TC (Q-4).
