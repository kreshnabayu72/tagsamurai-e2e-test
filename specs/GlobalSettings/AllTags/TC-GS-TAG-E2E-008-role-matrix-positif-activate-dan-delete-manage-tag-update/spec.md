---
id: TC-GS-TAG-E2E-008-role-matrix-positif-activate-dan-delete-manage-tag-update
title: "Role Matrix Positif: Manage TAG (Update) Menyelesaikan Activate TAG dan Menghapus Tag Available"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-31
  - TC-GS-TAG-33
coverage:
  web: automated
---

# Role Matrix Positif: Manage TAG (Update) Menyelesaikan Activate TAG dan Menghapus Tag Available

## Prerequisites

- Mode: FE+BE.
- Akun aktor: lihat tabel "Role yang diuji" di bawah. Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`). Password `Spectra.env.GS_TAG_UPDATE_PASSWORD` belum terdaftar di `.env.example` dan `spectra.config.ts`; dicatat di `suite.md` bagian Kredensial.
- Data: Seed Registri A (DD-01 s.d. DD-30; DD-02 `E2801160600002054D8A0002` Available dipakai sebagai target Delete TC-33), stok resmi Admin Console Client A DD-S1 (GPS `356938035643001`, Available; Device Name `Teltonika FMB920`), kuota GPS Client A tersedia (1 of 30 terpakai). Seed dan stok di-seed ulang idempotent oleh hook `before` (Q-4; mekanisme disediakan tim FE/BE). Tag hasil Activate (`356938035643001`) dan DD-02 yang dihapus dikembalikan ke kondisi awal oleh reset seed pada hook `after`.
- Role yang diuji: hanya Manage TAG (Update), sesuai TC sumber (Role Matrix positif). Total Control tidak diuji karena TC-31 dan TC-33 hanya menyebut Manage TAG (Update); lihat Temuan untuk QA.

Role yang diuji (Tabel Data Uji Pre-setup; Client A):

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-31, TC-33 | Manage TAG (Update) | Agus Wijaya | `manageTagUpdate_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TAG_UPDATE_PASSWORD` |

- Layar awal: Global Settings > TAG Tab All dibuka di hook `beforeEach`.
- Guided Tooltip: flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Selektor: radio overlay Select TAG Type, input entri manual GPS dan tombol `Add` (label/placeholder menunggu desain, NC-11) belum punya ID/aria-label di sumber; diselesaikan tim FE di tahap script.
- State global: tidak ada yang diubah selain data registri (dipulihkan seperti di atas). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-TAG-31: Manage TAG (Update) menyelesaikan Activate TAG sampai sukses

1. Klik `+ Activate TAG`
2. Pilih `GPS` pada overlay `Select TAG Type`
3. Klik `Continue` pada popup `Ready to Activate a TAG`
4. Ketik `356938035643001` di input entri manual, klik `Add`
5. Klik `Submit`
6. Klik `Submit` pada dialog `Submit Activation`
7. Verifikasi toast sukses `Success, TAG has been activated.`
8. Tunggu toast hilang otomatis
9. Klik item sidebar `TAG`, klik Tab All
10. Ketik Search `356938035643001`, tekan Enter
11. Verifikasi tag `356938035643001` muncul di registri berstatus Available
12. Klik `(←)` pada kotak Search

### TC-GS-TAG-33: Manage TAG (Update) menghapus tag Available lewat menu baris

13. Verifikasi tag DD-02 `E2801160600002054D8A0002` tampil di registri dengan Status Available
14. Buka menu baris DD-02, klik `Delete`
15. Klik `Delete` pada dialog `Delete TAG`
16. Verifikasi toast sukses `Success, TAG has been deleted.`
17. Ketik Search `E2801160600002054D8A0002`, tekan Enter
18. Verifikasi empty state `No results found`
19. Verifikasi baris DD-02 hilang dari registri

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md` (Section 2). Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan: TC-31 (menambah data) sebelum TC-33 (menghapus data); sesuai urutan sumber. Delete di akhir spec (prinsip 5). Langkah 8, 9, 12 adalah langkah penghubung tanpa `Verifikasi` (S-03); langkah 9 (sidebar `TAG`, Tab All) membawa pelaku kembali ke registri karena halaman Activate tetap terbuka sesudah Submit berhasil; langkah 13 adalah precondition TC-33 (c) yang diasersi sebagai anchor.
- Langkah 18 (`No results found`) adalah anchor positif yang sah untuk absence hasil Search (8b butir 2), ditambah toast sukses langkah 16 sebagai anchor respons server; langkah 19 adalah kesimpulan Expected b dan diasersi pada langkah itu.
- Rujukan lintas spec: TC-32 (Manage TAG Update menyelesaikan Audit TAG) ada di spec 042 karena butuh harness scan; spec ini hanya memuat TC-31 dan TC-33.
- Spec memuat blok pembuat data (TC-31, mengaktivasi `356938035643001`) dan blok bukan pembuat data (TC-33, menghapus DD-02 dari seed): keduanya aksi tulis satu role (Manage TAG (Update)) pada satu registri dan satu login Role Matrix positif (bagian 3a); TC-33 tidak memakai hasil TC-31 sehingga kegagalan blok TC-31 tidak membuat blok TC-33 kehilangan makna, blok Delete ada di akhir (prinsip 5), dan pembersihan kedua blok dilakukan reset seed pada hook `after`.
- Temuan untuk QA:
  - TC-31 dan TC-33 mensyaratkan hanya Manage TAG (Update); Total Control belum punya TC positif per aksi Activate/Delete untuk Role Matrix (usulan TC baru jika diperlukan).
  - TC-33 menghapus DD-02, baris Pre-setup bersama (S-06); dipulihkan lewat reset seed dan dicatat di Prerequisites (TC tidak menyediakan data milik spec).
  - TC-31 Post Condition (tag `356938035643001` Available) diasersi lewat langkah 11 sebagai bagian Expected b.
