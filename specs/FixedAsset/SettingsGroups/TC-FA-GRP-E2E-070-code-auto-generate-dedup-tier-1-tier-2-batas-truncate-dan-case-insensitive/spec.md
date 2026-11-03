---
id: TC-FA-GRP-E2E-070-code-auto-generate-dedup-tier-1-tier-2-batas-truncate-dan-case-insensitive
title: "Code Auto-Generate: Dedup Tier 1 Suffix Angka, Tier 2 ParentCode, Batas 5 Percobaan, Truncate 15 Karakter, dan Keunikan Case-Insensitive"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-GRP-329
  - TC-FA-GRP-330
  - TC-FA-GRP-331
  - TC-FA-GRP-332
  - TC-FA-GRP-333
  - TC-FA-GRP-1064
coverage:
  web: automated
---

# Code Auto-Generate: Dedup Tier 1 Suffix Angka, Tier 2 ParentCode, Batas 5 Percobaan, Truncate 15 Karakter, dan Keunikan Case-Insensitive

## Prerequisites

- Mode: FE+BE (backend nyata; Code auto-generate dan dedup dihitung server saat Create dan dibaca di tabel).
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.FA_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data Pre-setup (hanya dibaca): Client automation Plan Professional (Pre-setup No 8) dengan jumlah group di bawah cap; pohon group Tabel A, termasuk Head Office (level 1) yang punya child Floor 2.
- Data Pre-setup (hanya dibaca): Head Office (Code `HO`), Server Room (Code `SR`), dan Warehouse A (Code `WH-A`). Code `HO` dan `SR` yang sudah dipakai Pre-setup menjadi bagian dari precondition TC-FA-GRP-329, 330, 331, dan 1064.
- Data Dinamis (nama literal karena Code auto-generate diturunkan dari token Name; seeding lewat API di hook `before`, dibersihkan di hook `after`):
  - TC-FA-GRP-329: group seed ber-Code `HO2` (`HO2 Seed {runId}-070`); Name uji `Home Office` (inisial `HO`).
  - TC-FA-GRP-330: group seed ber-Code `SR2`, `SR3`, `SR4`, `SR5`, `SR6` (`SR2 Seed {runId}-070` dan seterusnya); Name uji `Store Room` (inisial `SR`) di bawah Warehouse A (Code `WH-A`).
  - TC-FA-GRP-1064: group seed ber-Code `SR2` sampai `SR5` saja (`SR6` bebas); Name uji `Store Room` di bawah Warehouse A.
  - TC-FA-GRP-331: group seed `Long Parent {runId}-070` ber-Code `ABCDEFGHIJKLMN` (14 karakter); group seed ber-Code `SR2` sampai `SR6`; Name uji `Store Room` di bawah `Long Parent {runId}-070`.
  - TC-FA-GRP-332: group seed ber-Code `ABCDEFGHIJKLMNO` (15 karakter, kandidat 16 inisial yang dipotong); Name uji 16 kata berinisial `A` sampai `P`: `Alpha Bravo Charlie Delta Echo Foxtrot Golf Hotel India Juliet Kilo Lima Mike November Oscar Papa`.
  - TC-FA-GRP-333: group seed ber-Code manual `ro` (tersimpan `RO`; `Seed RO {runId}-070`); Name uji `Research Office` (inisial `RO`).
- Kemampuan teknis: tidak ada selain pembacaan kolom Code di tabel Groups List; pemulihan state SR (hapus `Store Room` hasil uji dan seed `SR6`) lewat API pada langkah penghubung.
- Pemulihan (hook `before` dan `after`): hapus lewat API semua group seed dan hasil uji spec ini (nama literal `Home Office`, `Store Room`, `Research Office`, nama 16 kata, dan seed ber-Code `HO2`, `SR2` sampai `SR6`, `ABCDEFGHIJKLMN`, `ABCDEFGHIJKLMNO`, `RO`, serta hasil `HO3`, `WH-A-SR`, `SR6`, `SR7`, `RO2`); hook `before` juga menghapus sisa literal run sebelumnya.
- State global: tidak ada yang diubah.

## Test Steps

### TC-FA-GRP-329: Dedup Tier 1 suffix angka

1. Klik [+] Group di sidebar, isi Group Name `Home Office` dengan Code kosong, lalu klik [Submit]
2. Ketik Search `Home Office`, tekan Enter
3. Verifikasi Code tersimpan `HO3` (HO dan HO2 sudah dipakai)

### TC-FA-GRP-330: Dedup Tier 2 ParentCode setelah lebih dari 5 percobaan

4. Ganti isi kotak Search dengan `Warehouse A`, tekan Enter
5. Klik Add Subgroup pada baris Warehouse A di tabel, isi Group Name `Store Room` dengan Code kosong, lalu klik [Submit]
6. Ganti isi kotak Search dengan `Store Room`, tekan Enter
7. Verifikasi Code tersimpan `WH-A-SR` (6 percobaan Tier 1 habis: `SR`, `SR2` sampai `SR6` dipakai)
8. Hapus `Store Room` hasil uji dan seed `SR6` lewat API

### TC-FA-GRP-1064: Tepat di batas, 5 percobaan Tier 1 terpakai, percobaan ke-6 masih Tier 1

9. Ganti isi kotak Search dengan `Warehouse A`, tekan Enter
10. Klik Add Subgroup pada baris Warehouse A di tabel, isi Group Name `Store Room` dengan Code kosong, lalu klik [Submit]
11. Ganti isi kotak Search dengan `Store Room`, tekan Enter
12. Verifikasi Code tersimpan `SR6` (Tier 1 belum gagal lebih dari 5 percobaan)
13. Verifikasi Code tidak berformat `WH-A-SR`

### TC-FA-GRP-331: ParentCode 14 karakter atau lebih melewati Tier 2

14. Ganti isi kotak Search dengan `Long Parent {runId}-070`, tekan Enter
15. Klik Add Subgroup pada baris `Long Parent {runId}-070`, isi Group Name `Store Room` dengan Code kosong, lalu klik [Submit]
16. Ganti isi kotak Search dengan `Store Room`, tekan Enter
17. Verifikasi Code tersimpan `SR7` (lanjut suffix angka Tier 1)

### TC-FA-GRP-332: Truncate ke 15 karakter tanpa memotong suffix

18. Klik [+] Group di sidebar, isi Group Name 16 kata berbeda inisial dengan Code kosong, lalu klik [Submit]
19. Ketik Search nama 16 kata tersebut, tekan Enter
20. Verifikasi Code akhir paling banyak 15 karakter
21. Verifikasi suffix angka tetap utuh di akhir Code dan bagian kandidat yang dipotong

### TC-FA-GRP-333: Keunikan case-insensitive terhadap Code manual lowercase

22. Klik [+] Group di sidebar, isi Group Name `Research Office` dengan Code kosong, lalu klik [Submit]
23. Ketik Search `Research Office`, tekan Enter
24. Verifikasi Code tersimpan `RO2` (Code manual `ro` tersimpan `RO` sudah dipakai)
25. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Urutan TC: TC-FA-GRP-329, 330, lalu TC-FA-GRP-1064, 331, 332, 333; berbeda dari urutan nomor TC sumber. Urutan SR dipilih supaya state seed konsisten: TC-FA-GRP-330 membutuhkan `SR` sampai `SR6` terpakai; sesudah langkah 8 hanya `SR` sampai `SR5` terpakai (precondition TC-FA-GRP-1064); TC-FA-GRP-1064 menghasilkan `SR6` sehingga `SR` sampai `SR6` terpakai kembali untuk TC-FA-GRP-331 (S-09).
- Nama `Store Room` dipakai berulang di bawah Warehouse A (TC-FA-GRP-330 dan TC-FA-GRP-1064); hasil TC-FA-GRP-330 dihapus di langkah 8 supaya nama tidak duplikat sibling.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 2 (Ketik Search `Home Office`, tekan Enter); langkah 6 (Ganti isi kotak Search dengan `Store Room`, tekan Enter); langkah 8 (Hapus `Store Room` hasil uji dan seed `SR6` lewat API); langkah 11 (Ganti isi kotak Search dengan `Store Room`, tekan Enter); langkah 16 (Ganti isi kotak Search dengan `Store Room`, tekan Enter); langkah 19 (Ketik Search nama 16 kata tersebut, tekan Enter); langkah 23 (Ketik Search `Research Office`, tekan Enter); langkah 25 (Klik `(←)` pada kotak Search).
- Pencarian baris target (S-03, R-16): langkah 4, 9, 14 (Ganti isi kotak Search dengan `Warehouse A` dan `Long Parent {runId}-070`, tekan Enter) menemukan baris yang dipakai Add Subgroup; client memiliki lebih dari 10 node level 1 dan page size 10, jadi baris target tidak dijamin berada di halaman 1 All Groups.
- Temuan untuk QA:
  - Code Server Room Pre-setup adalah `SR` (Tabel A baris 9); precondition TC-FA-GRP-330, 331, dan 1064 yang menyebut "SR sudah dipakai" dipenuhi oleh Pre-setup, sedangkan TC-FA-GRP-326 (spec 069) menyebut `SR` belum dipakai. Dua TC ini saling bertentangan.
  - TC-FA-GRP-332 tidak menyebut nama 16 kata, Code seed, maupun Code akhir yang diharapkan; spec memakai Code akhir paling banyak 15 karakter dengan suffix angka utuh dan nama 16 kata `A` sampai `P` yang dipilih penulis.
  - TC-FA-GRP-332 Expected "suffix tetap utuh" tidak menyebut nilai suffix; spec tidak menegaskan angka suffix.
  - TC-FA-GRP-333 menyebut Code manual `ro` sebagai precondition tanpa menyebut cara membuatnya; spec men-seed lewat API.
  - Name `Home Office`, `Store Room`, `Research Office`, dan nama 16 kata harus literal karena token Name menentukan Code; suffix per run mengubah hasil. Butuh butir Lampiran A modul Groups (S-12).

