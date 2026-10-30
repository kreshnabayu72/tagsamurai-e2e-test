---
id: TC-GS-UCF-E2E-025-form-user-numeric-normalisasi-nilai-tersimpan
title: "Form User: Normalisasi Nilai Numeric yang Tersimpan (Nol di Depan, Titik, Negatif Nol, Nol di Belakang)"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-UCF-378
  - TC-GS-UCF-382
  - TC-GS-UCF-383
  - TC-GS-UCF-384
  - TC-GS-UCF-385
  - TC-GS-UCF-386
  - TC-GS-UCF-387
  - TC-GS-UCF-495
  - TC-GS-UCF-496
coverage:
  web: automated
---

# Form User: Normalisasi Nilai Numeric yang Tersimpan (Nol di Depan, Titik, Negatif Nol, Nol di Belakang)

## Prerequisites

- Mode: FE+BE (backend nyata). Cakupan lintas modul: field Custom Field Numeric pada form Create User dan tampilan Detail User (modul User).
- Akun aktor: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`; environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_<page_key>` disetel true oleh hook suite `before` untuk akun aktor dan dipulihkan di hook `after` (dinyatakan di `suite.md`).
- Layar awal: Global Settings > User > User List sub-tab Login User, dibuka di hook `beforeEach`.
- Data Pre-setup (di-seed lewat API di hook `before`, idempotent, fixture `Fixture.customFieldUser.preset14` (fixture baru, belum ada; lihat coverage); hanya dibaca): 14 Custom Field aktif Client A (D-01): 6 Pre-setup (`Cost Center` Dropdown `Finance`, `Operations`, `Marketing`, Required Yes; `Employee Grade`; `Job Description`; `Bonus` Numeric Decimal Places 2; `Office Phone` Phone Required Yes; `Joining Date` [Inactive]) dan 8 Population (`Blood Type`, `Shirt Size`, `Emergency Phone`, `Birth Date`, `Tax ID` Text Required Yes, `Work Notes`, `Annual Target`, `badge number`). Hanya `Bonus` yang diasersi; `Cost Center`, `Office Phone`, dan `Tax ID` diisi sebagai Custom Field Required; field lain dipakai sebagai precondition TC (14 field aktif), tidak diasersi.
- Kondisi D-158 (precondition TC): Custom Field Required Yes yang Active di Client A hanya `Cost Center`, `Office Phone`, dan `Tax ID`; dijamin oleh hook `before` suite (butir D-158 di `suite.md`: Custom Field Required Yes Active selain yang disebut dinonaktifkan atau dihapus lewat API sebelum spec berjalan dan dipulihkan di hook `after` suite; mekanisme disediakan tim FE/BE); spec ini tidak mengubah status field.
- Field wajib Create User (fixture form, tabel Data Uji Pre-setup TC): First Name `Probe`, Last Name `Custom`, Email `probeCustom<nomor TC>_automated_qaTeam1+{runId}-025@qwertysystem.net` (`{runId}` terdiri atas digit), Division = Division Client A mana pun (fixture modul Division, disediakan tim FE), Access = opsi pertama yang tersedia untuk Client A; field User opsional dikosongkan. Custom Field Required: Cost Center `Finance`, Office Phone Country Code `🇮🇩 +62` dengan Number `81234567890`, Tax ID `TX-001`.
- Data dinamis (user dibuat lewat UI; satu user per baris tabel, satu nilai khusus Bonus per user), parameter loop langkah 1 sampai 8:

  | No | TC | Email (bagian `<nomor TC>`) | Input Bonus (Decimal Places 2) | Nilai tersimpan di Detail User |
  |---|---|---|---|---|
  | 1 | TC-GS-UCF-378 | probeCustom378 | `007.5` | `7.5` |
  | 2 | TC-GS-UCF-382 | probeCustom382 | `.5` | `0.5` |
  | 3 | TC-GS-UCF-383 | probeCustom383 | `5.` | `5` |
  | 4 | TC-GS-UCF-384 | probeCustom384 | `-0` | `0` |
  | 5 | TC-GS-UCF-385 | probeCustom385 | `5` | `5` (bukan `5.00`) |
  | 6 | TC-GS-UCF-386 | probeCustom386 | `-0.0` | `0.0` |
  | 7 | TC-GS-UCF-387 | probeCustom387 | `5.50` | `5.50` |
  | 8 | TC-GS-UCF-495 | probeCustom495 | `00` | `0` |
  | 9 | TC-GS-UCF-496 | probeCustom496 | `000` | `0` |

- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): hapus lewat API semua user Client A dengan Email yang memuat `{runId}-025`.
- Kemampuan teknis: membuka Detail User (section Custom Fields) dari modul User berdasarkan Email; pembacaan teks nilai Custom Field di Detail User.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

### Untuk setiap baris tabel (langkah 1 sampai 8, diulang 9 kali; TC pada kolom TC)

1. Klik [+ User] pada tab User List sub-tab Login User
2. Isi Field wajib Create User (First Name `Probe`, Last Name `Custom`, Email baris) dan Custom Field Required (Cost Center `Finance`, Office Phone `🇮🇩 +62` dengan Number `81234567890`, Tax ID `TX-001`)
3. Isi Bonus dengan Input Bonus baris
4. Klik [Submit]
5. Verifikasi tidak ada error inline pada Bonus
6. Buka Global Settings > User > Detail User dengan Email baris, section Custom Fields
7. Verifikasi user tersimpan: Detail User `Probe Custom` terbuka
8. Verifikasi Bonus pada Detail User menampilkan persis Nilai tersimpan baris

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Pengulangan: langkah 1 sampai 8 diulang untuk sembilan baris tabel (TC-GS-UCF-378, 382, 383, 384, 385, 386, 387, 495, 496), diurutkan sama dengan urutan TC pada kolom sourceTc. Ambang 35 langkah dihitung dengan ekspansi (8 langkah × 9 baris = 72 langkah). Alasan (bagian 3 prinsip 13 dan bagian 8b butir 7): semua baris satu topik (normalisasi nilai Numeric), satu akun, satu dataset, langkah identik, dan hanya nilai Bonus yang berbeda; parameter ada di tabel Prerequisites tanpa langkah bersyarat; `Verifikasi` yang diulang tetap satu per klausa. Satu nilai khusus per user (prinsip 9) sehingga penyebab kegagalan jelas dan baris yang gagal tidak membuat baris lain kehilangan makna.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 sampai 4 dan langkah 6 (membuka form, mengisi, mengirim, dan membuka Detail User sebagai bagian langkah TC).
- Langkah 4 tidak diikuti langkah "Tunggu aksi selesai" karena langkah 5 dan 6 membaca hasil di surface yang sama dan Detail User dibuka berdasarkan Email.
- Asersi tampil "bukan `5.00`" (TC-GS-UCF-385) dan "tanda minus dibuang" (TC-GS-UCF-384, 386) tercakup oleh asersi nilai persis di langkah 8.
- Temuan untuk QA:
  - Expected TC-GS-UCF-378 sampai 387 dan 495 sampai 496 tidak menyebut toast Create User; hanya "tidak ada error inline; user tersimpan" dan nilai di Detail User. Langkah 7 mengasersi "user tersimpan" lewat Detail User yang terbuka; teks toast Create User (modul User) tidak diasersi.
  - Cara membuka Detail User berdasarkan Email tidak ditulis di TC ("Buka Global Settings > User > Detail user dengan Email ..."); mengikuti alur modul User (disediakan tim FE).
  - TC-GS-UCF-386 mengharapkan `0.0` sementara TC-GS-UCF-384 mengharapkan `0`; spec mengikuti masing-masing TC tanpa menyimpulkan aturan normalisasi sendiri.
