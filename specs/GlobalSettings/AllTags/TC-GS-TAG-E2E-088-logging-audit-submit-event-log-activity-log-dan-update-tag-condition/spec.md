---
id: TC-GS-TAG-E2E-088-logging-audit-submit-event-log-activity-log-dan-update-tag-condition
title: "Pencatatan Audit Submit: Event Log, Activity Log Audit TAG, dan Update TAG Condition per Tag yang Berubah"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-265
  - TC-GS-TAG-266
coverage:
  web: automated
---

# Pencatatan Audit Submit: Event Log, Activity Log Audit TAG, dan Update TAG Condition per Tag yang Berubah

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Client Audit Joko Santoso `totalControl_automated_qaAudit@qwertysystem.net` (Tabel Data Uji Pre-setup TC); kredensial `Spectra.env.GS_TC_AUDIT_PASSWORD` (belum terdaftar di `.env.example` dan `spectra.config.ts`; perlu didaftarkan pemilik repositori, tanpa nilai). Login sekali di hook `before` spec ini; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `Spectra.env.GS_TC_PASSWORD`).
- Flag Guided Tooltip `gs-tag-registry` dan `gs-tag-activate` mengikuti hook suite `before` dan `after` (lihat `suite.md`, bagian Hook Guided Tooltip).
- Suite serial (`parallel: false`). Hook `beforeEach`: buka Global Settings > TAG, Tab Not Paired.
- Hook `after` suite memulihkan Seed Client Audit (AU1 sampai AU7 dan sibling NFC `04A224B2C15E95`) secara idempotent (pernyataan hook di `suite.md`).
- Data Pre-setup (Seed Client Audit, Tabel Data Uji Dinamis TC; dipulihkan ke kondisi awal oleh hook `before` dan sebelum langkah 22 lewat fixture BE; mekanisme disediakan tim FE/BE, lihat Temuan untuk QA): tag RFID Object `E2801160600002054D8A5001` (AU1, Available, combined dengan NFC `04A224B2C15E95` Available), `E2801160600002054D8A5002` (AU2, Damaged/Missing), `E2801160600002054D8A5003` (AU3, Retired), `E2801160600002054D8A5004` (AU4, Available), `E2801160600002054D8A5005` (AU5, Reserved), `E2801160600002054D8A5006` (AU6, Paired), `E2801160600002054D8A5007` (AU7, To be Returned).
- Kemampuan teknis (disediakan tim FE): simulasi pemindai RFID (pindai kode, `Stop` pada Floating Status Widget sebelum menyentuh kontrol halaman lain; page-lock sesi scan, NC-43; label TC `Manual Only — (b)` bukan alasan mengeluarkan TC, keputusan D-4, Q-1).
- Baseline log: Event Log dan Activity Log menumpuk antar spec (tidak dibersihkan) dan identifier tag bersifat tetap, sehingga N tidak diturunkan dari seeding: total dibaca dari footer pagination (pembaca nilai footer Event Log dan Activity Log) sebelum aksi, dan semua asersi entri baru memakai selisih total terhadap baseline itu (S-12).
- Tabel "Tag Update TAG Condition TC-265" (parameter langkah 3 sampai 5 dan 17 sampai 21):

| Tag | Code | Old Value | New Value |
|---|---|---|---|
| AU2 | `E2801160600002054D8A5002` | `Damaged/Missing` | `Available` |
| AU1 | `E2801160600002054D8A5001` | `Available` | `Damaged/Missing` |
| Sibling NFC AU1 | `04A224B2C15E95` | `Available` | `Damaged/Missing` |
| AU4 | `E2801160600002054D8A5004` | `Available` | `Damaged/Missing` |

- Aturan baca total entri Activity Log setelah Search (berlaku untuk langkah 5, 25, dan 34): total dibaca dari footer `Showing ... of N` bila ada baris, dan bernilai 0 bila tampil empty state `No results found`.
- Tabel "Tag diamati TC-266" (parameter langkah 23 sampai 25 dan 32 sampai 34): `AU1` `E2801160600002054D8A5001`, `AU2` `E2801160600002054D8A5002`, `AU3` `E2801160600002054D8A5003`, `AU4` `E2801160600002054D8A5004`.
- State global yang diubah: tidak ada selain data (Seed Client Audit dan log).

## Test Steps

### TC-GS-TAG-265: Audit Submit, Event Log, Activity Log Audit TAG, dan Update TAG Condition per tag yang berubah

1. Klik tombol `Event Log`, klik tab `Audit TAG`, catat total `M0` pada footer (`Showing ... of M0 logs`), lalu tutup modal lewat `✕`
2. Buka Global Settings > Activity Log, tab User Action, filter Action `Audit TAG`, catat total entri `A0` pada footer
3. Untuk setiap baris tabel "Tag Update TAG Condition TC-265", lakukan langkah 4 sampai 5
4. Filter Action `Update TAG Condition`, ketik Search Code tag, tekan Enter
5. Catat total entri `B` tag itu (aturan baca total di Prerequisites), lalu klik `(←)` pada kotak Search
6. Buka Global Settings > TAG, Tab Not Paired
7. Klik `Audit TAG`, pilih `RFID` pada overlay `Select TAG Type`
8. Pindai AU2 saja (`E2801160600002054D8A5002`), lalu klik `Stop` pada Floating Status Widget
9. Klik `Submit`, biarkan checkbox `Mark all as Damaged/Missing` dicentang, klik `Confirm`
10. Tunggu aksi selesai
11. Buka Event Log, klik tab `Audit TAG`
12. Verifikasi total log menjadi `M0 + 1`
13. Verifikasi baris pertama (Date terbaru): TAG Type `RFID`, Found `1`, Not Found `3`, Not Found Action `Marked as Damaged/Missing`
14. Tutup modal lewat `✕`, buka Global Settings > Activity Log, tab User Action, filter Action `Audit TAG`
15. Verifikasi total entri bertambah tepat 1 menjadi `A0 + 1` (satu entri per operasi, bagian 8.1 PRD)
16. Verifikasi entri teratas (Date terbaru): Name `RFID`, Field `Status`, Old Value `—`, New Value `Verified 1, Not Scanned 3, Mark all as Damaged/Missing: Yes`
17. Untuk setiap baris tabel "Tag Update TAG Condition TC-265", lakukan langkah 18 sampai 21
18. Filter Action `Update TAG Condition`, ketik Search Code tag, tekan Enter
19. Verifikasi total entri tag itu menjadi `B + 1`
20. Verifikasi entri teratas memuat Name = Code tag, Field `Status`, Old Value dan New Value sesuai tabel
21. Klik `(←)` pada kotak Search

### TC-GS-TAG-266: Audit Submit tidak mencatat Update TAG Condition untuk tag yang statusnya tidak berubah

22. Pulihkan Seed Client Audit lewat fixture BE ke kondisi awal (AU1 sampai AU7 dan sibling NFC `04A224B2C15E95` seperti Prerequisites)
23. Untuk setiap baris tabel "Tag diamati TC-266", lakukan langkah 24 sampai 25
24. Buka Global Settings > Activity Log, tab User Action, filter Action `Update TAG Condition`, ketik Search Code tag, tekan Enter
25. Catat total entri `C` tag itu (aturan baca total di Prerequisites), lalu klik `(←)` pada kotak Search
26. Buka Global Settings > TAG, Tab Not Paired, klik `Audit TAG`, pilih `RFID`, lalu pindai AU1 dan AU4 (Available), pindai AU2 dan AU3, dan klik `Stop` pada Floating Status Widget
27. Klik `Submit`
28. Tunggu aksi selesai, lalu buka Global Settings > Activity Log, tab User Action, filter Action `Update TAG Condition`
29. Ketik Search Code AU2 (`E2801160600002054D8A5002`), tekan Enter
30. Verifikasi total entri AU2 menjadi `C + 1`
31. Verifikasi entri teratas AU2: Old Value `Damaged/Missing` dan New Value `Available`
32. Untuk setiap tag AU1, AU3, dan AU4 pada tabel "Tag diamati TC-266", lakukan langkah 33 sampai 34
33. Ganti isi kotak search dengan Code tag itu, tekan Enter
34. Verifikasi total entri tag itu sama dengan `C` yang dicatat pada langkah 25 (tidak ada entri baru; aturan baca total di Prerequisites)

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Subjudul `###` memetakan langkah ke id TC granular. Kelas d (scan).
- Urutan TC dalam spec sama dengan sumber (265, 266). Fixture direset sebelum TC-266 (langkah 22) karena TC-265 mengubah status AU1, AU2, AU4, dan sibling NFC.
- Kelas g ringan (klausa "tidak ada entri untuk AU1, AU3, AU4", langkah 33 sampai 34) ditulis di spec asal dengan baseline `C` sesuai keputusan D-1; tidak ada spec absence terpisah. P-1 (state berat): asersi bergantung pada sesi Audit yang baru dibangun langkah 26 sampai 27 (S-05); anchor positif adalah entri AU2 pada langkah 30 dan 31 (bagian 8b butir 2).
- Alasan spec di atas sekitar 35 langkah (34 langkah tertulis, sekitar 62 setelah ekspansi tabel): dua TC memakai satu alur (Audit RFID Client Audit dengan scan tersimulasi) dan dua surface log yang sama; langkah berulang per tag memakai parameter di tabel Prerequisites tanpa langkah bersyarat (bagian 8b butir 7). Langkah yang diulang: 3 sampai 5 (empat iterasi), 17 sampai 21 (empat iterasi), 23 sampai 25 (empat iterasi), 32 sampai 34 (tiga iterasi).
- `Verifikasi` yang diulang tetap satu per klausa (S-01). Langkah penghubung (tanpa `Verifikasi`, tidak ada di TC): langkah 1 sampai 5, 23 sampai 25 (pencatatan baseline sebelum aksi pemicu), langkah 6, 14, 28 (pindah surface), langkah 10 (Tunggu aksi selesai), langkah 21 dan 33 (mengosongkan atau mengganti isi kotak search), langkah 22 (reset fixture; precondition TC-266), langkah 8 dan 26 (`Stop` pada Floating Status Widget, konvensi `Pindai X` di Catatan TC).
- Sibling NFC `04A224B2C15E95` tidak dipindai dan tidak dihitung pada Found/Not Found (Expected a dan c TC-265 mengikuti PRD §3.2 langkah 3: sibling combined silent).
- Temuan untuk QA:
  - TC-265 dan TC-266 berlabel `Manual Only — (b)`; cara simulasi pemindai tidak didefinisikan di TC, PRD, atau LLD (Q-1); disediakan tim FE tanpa endpoint karangan.
  - Seeding dan reset Seed Client Audit antar blok tidak didefinisikan di TC (Q-4).
  - TC-265 Expected c menyebut `Update TAG Condition` untuk sibling NFC `04A224B2C15E95` tanpa menyebut bahwa sibling tidak dihitung pada `Not Found` (3 = AU1, AU3, AU4); spec mengikuti angka TC.
  - TC-265 Expected tidak menyebut kolom Object entri `Audit TAG` dan `Update TAG Condition`; spec tidak mengasersi kolom Object.
  - TC-266 langkah 4 (`Submit`) tidak menyebut dialog `Submit Audit` karena semua tag terpindai; spec tidak mengasersi ada atau tidaknya dialog.
