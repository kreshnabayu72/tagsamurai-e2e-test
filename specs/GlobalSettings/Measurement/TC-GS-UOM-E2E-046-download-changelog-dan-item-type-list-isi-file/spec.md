---
id: TC-GS-UOM-E2E-046-download-changelog-dan-item-type-list-isi-file
title: "Download Changelog dan Item Type List: Isi dan Nama File"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-188
  - TC-GS-UOM-195
coverage:
  web: automated
---

# Download Changelog dan Item Type List: Isi dan Nama File

## Prerequisites

- Mode: FE+BE. Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Flag Guided Tooltip halaman Measurement mengikuti pernyataan hook suite di `suite.md`.
- Fixture: `fixtures/measurement.json` belum ada; tim FE menyiapkannya (lihat `suite.md`, bagian Data bersama).
- Akun: Total Control Client A, Sari Dewi (Sari D), `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > Master Reference > Measurement dilakukan sekali di hook `before` suite.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (hanya dibaca): Pieces / pc memiliki 3 Item Type pada accordion Item Type List (FAMS: Laptop, Monitor; Supply: Printer Ink).
- Data milik spec (klien HTTP/API disediakan tim FE): unit `Unit Log {runId}-046` dengan Symbol `ul046`, dibuat lalu dihapus lewat API di hook `before` supaya Changelog Measurement memuat entri Create dan Delete untuk unit itu (dipakai sebagai precondition TC-GS-UOM-188 "Changelog memiliki entri Delete", tidak diasersi selain lewat isi berkas). Unit sudah terhapus saat spec berjalan; hook `after` menghapusnya bila masih ada.
- Jumlah entri Changelog total tidak diasersi sebagai angka absolut (S-12); asersi memakai entri milik spec.
- State global yang dipulihkan: Filter Modal Changelog dikosongkan dan modal ditutup di hook `beforeEach`; berkas unduhan dihapus di hook `after`.
- Hook `beforeEach`: buka Global Settings > Master Reference > Measurement.
- Kemampuan teknis (kelas binary buffer, prinsip 13f): menangkap berkas unduhan browser ke direktori bersih per unduhan; membaca isi berkas CSV dan XLSX (nama kolom, jumlah baris, nilai sel kolom Action dan Unit Name).

## Test Steps

### TC-GS-UOM-188: Download Changelog tanpa dan dengan Filter

1. Klik Changelog
2. Klik Download, lalu klik `Download CSV`
3. Verifikasi file `Changelog-Measurement.csv` terunduh
4. Verifikasi file `Changelog-Measurement.csv` memuat baris Create dan baris Delete untuk `Unit Log {runId}-046` (tidak terbatas satu Action)
5. Klik Filter, pilih Action `Delete`
6. Klik [Apply]
7. Klik Download, lalu klik `Download XLSX`
8. Verifikasi file `Changelog-Measurement.xlsx` terunduh
9. Verifikasi file `Changelog-Measurement.xlsx` memuat baris Delete untuk `Unit Log {runId}-046`
10. Verifikasi seluruh baris pada `Changelog-Measurement.xlsx` ber-Action Delete
11. Verifikasi `Changelog-Measurement.xlsx` tidak memuat baris Create untuk `Unit Log {runId}-046`
12. Tutup Modal Changelog lewat `[✕]`

### TC-GS-UOM-195: Download Item Type List

13. Ketik Search `Pieces`, tekan Enter
14. Buka Detail Pieces (klik link Unit Name `Pieces`)
15. Klik Download, lalu klik `Download XLSX`
16. Verifikasi tidak ada toast sukses
17. Verifikasi file `Item Types - Pieces.xlsx` terunduh berisi 3 baris data
18. Tutup Modal Unit Detail lewat `[✕]`
19. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): penutupan Modal Changelog dan Modal Unit Detail di akhir tiap blok; langkah 13 (Search `Pieces`: baris `Pieces` berada di halaman 2 pada tabel baseline 20 unit suite, S-14) dan langkah 19 (`(←)` pada kotak Search).
- Seeding minimal: entri Create dan Delete `Unit Log {runId}-046` dibuat lewat API hanya agar filter Action `Delete` pada TC-GS-UOM-188 bermakna; filter Action `Delete` Changelog tidak bergantung pada TC mutasi lain.
- Pencarian baris di berkas memakai nama unit bersuffix milik spec, bukan posisi baris (S-12).
- Berkas ditangkap ke direktori unduhan bersih per unduhan sehingga `Changelog-Measurement.csv` dan `Changelog-Measurement.xlsx` tidak tertimpa.
- Isi berkas Changelog dan Item Type List dipisah dari spec kegagalan export (kelas binary buffer, prinsip 13f). Kegagalan unduhan ada di spec 009.
- Semua TC sumber spec ini dikerjakan di sini; tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-UOM-188 Expected butir a "berisi seluruh baris Changelog": TC tidak menyatakan cara mengetahui total entri Changelog, dan total absolut tidak boleh diasersi (S-12). Spec membuktikan "tidak terbatas satu Action" lewat adanya baris Create dan Delete milik spec; kesesuaian jumlah baris dengan total entri tidak diasersi.
  - TC-GS-UOM-188 tidak menyebut cara membentuk entri Delete; spec menyiapkannya lewat API sebagai precondition.
  - TC-GS-UOM-195: Expected "berisi 3 baris" dihitung sebagai baris data tanpa header; TC tidak menyatakan.
  - Isi kolom dan format tanggal berkas Changelog tidak diasersi karena TC-GS-UOM-188 tidak memuat Expected terkait.
